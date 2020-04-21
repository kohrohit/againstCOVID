from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, serializers, viewsets, mixins
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from django.contrib.contenttypes.models import ContentType

from .serializers import ContentTypeSerializer


class ContentTypeViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAdminUser, ]
    authentication_classes = [OAuth2Authentication, ]
    serializer_class = ContentTypeSerializer
    queryset = ContentType.objects.all()


class ChoicesFullFormsView(generics.RetrieveAPIView):

    def retrieve(self, request, *args, **kwargs):
        # TODO: Add more choices as required

        from authentication.choices import AddressTagChoices, KYCDocumentTypeChoices, OrganizationTypeChoices

        data = dict()
        data[AddressTagChoices.__name__] = AddressTagChoices.values
        data[KYCDocumentTypeChoices.__name__] = KYCDocumentTypeChoices.values
        data[OrganizationTypeChoices.__name__] = OrganizationTypeChoices.values

        return Response(data)


class TransitionMapAPIView(APIView):
    permission_classes = [permissions.IsAdminUser, ]
    authentication_classes = [OAuth2Authentication, ]

    @staticmethod
    def __get_status_field(field_name, model_class):
        status_field = None
        for field in model_class._meta.get_fields():
            if field.name == field_name:
                status_field = field
                break
        return status_field

    def get(self, request):
        content_type_id = request.query_params.get('content_type_id', None)
        field = request.query_params.get('field', None)

        content_type = ContentType.objects.filter(id=content_type_id).first()

        if not (content_type and field):
            raise serializers.ValidationError("Please send content_type_id/ field")

        model_class = content_type.model_class()

        source_transition_mapping = {}
        field = field.strip().lower()
        status_field = self.__get_status_field(field, model_class)
        if status_field is None:
            raise serializers.ValidationError("Entered Field Name is not Valid for the Content Type")

        for transition in status_field.get_all_transitions(model_class):
            if transition.source not in source_transition_mapping:
                source_transition_mapping[transition.source] = {}
            source_transition_mapping[transition.source][transition.name] = transition.target

        return Response(source_transition_mapping)

