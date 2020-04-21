import json

from django_filters.rest_framework import DjangoFilterBackend
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import filters, generics, mixins, viewsets, status
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from miscellaneous.logging_utils import show_error
from miscellaneous.file_utils import upload_filestream_to_s3
from miscellaneous.mixins import CustomMetaDataMixin
from .models import Report, UploadedFile
from .serializers import ListReportSerializer, GetReportSerializer


class ListAllReportView(CustomMetaDataMixin, generics.ListAPIView):
    """
        Center App - This API is for list of all center data
    """
    queryset = Report.objects.all()
    serializer_class = ListReportSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_prepared', 'prepared_at', 'created_at', 'updated_at']
    search_fields = ['sid']
    pagination_class = LimitOffsetPagination


class GetReportView(CustomMetaDataMixin, generics.ListAPIView):
    """
        Reports App - Get Report using sid
    """
    queryset = Report.objects.all()
    serializer_class = GetReportSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        sid = request.data['sid']
        self.queryset = self.get_queryset().filter(sid=sid)[0]
        serializer = self.get_serializer(self.queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def generate_report(request):
    """
        Reports App - This API prompts AI engine to start generating report, and sends back 'sid' of report in response
    """
    response_body = {
        "meta": {
            "status": 1000,
            "is_error": False,
            "message": ""
        },
        "data": None
    }
    uploaded_files = []
    report = Report()
    try:
        # create a report object
        report.details = json.dumps({})
        report.save()

        # upload files to s3 & store files url
        files = request.FILES.getlist('files')
        if len(files) < 1:
            return Response('no upload files', status=status.HTTP_400_BAD_REQUEST)

        i = 0
        for file in files:
            i += 1
            file.name = '%s-%s' % (report.sid, i)
            uploaded_file = UploadedFile()
            uploaded_file.report = report
            uploaded_file.file = file
            uploaded_file.details = json.dumps({})

            try:
                bucket_file = upload_filestream_to_s3(file, file.name, 'uploads')
                uploaded_file.s3_url = bucket_file['url']
                uploaded_file.save()
                uploaded_files.append(uploaded_file)
            except Exception as e:
                print(e)
                return Response("files upload error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # prompt AI engine to start generating report
        # respond back with sid
        response_body['data'] = {'sid': report.sid}
        return Response(response_body, status=status.HTTP_200_OK)
    except Exception as e:
        show_error(e)
        try:
            report.delete()
            [f.delete() for f in uploaded_files]
        except:
            pass
        response_body['meta']['status'] = 500
        response_body['meta']['is_error'] = True
        response_body['meta']['message'] = "something went wrong"
        return Response(response_body, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
