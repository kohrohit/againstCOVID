from rest_framework import serializers

from reports.models import Report, UploadedFile


class ListReportSerializer(serializers.ModelSerializer):
    files = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = ('sid', 'is_prepared', 'prepared_at', 'details', 'files')

    def get_files(self, obj):
        files_data = []
        files = UploadedFile.objects.filter(report=obj.id)
        for file in files:
            files_data.append({
                'url': file.s3_url,
                'details': file.details
            })
        return files_data


class GetReportSerializer(serializers.ModelSerializer):
    """
    - This Serializer is for loading center's basic details in App
    - currently assuming that every center has one branch the rate,density,address,lat,lon are sent from the first branch
    """
    files = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = ('sid', 'is_prepared', 'prepared_at', 'details', 'files')

    def get_files(self, obj):
        files_data = []
        files = UploadedFile.objects.filter(report=obj.id)
        for file in files:
            files_data.append({
                'url': file.s3_url,
                'details': file.details
            })
        return files_data
