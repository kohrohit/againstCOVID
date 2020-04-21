from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import viewsets, permissions

from miscellaneous.mixins import CustomMetaDataMixin
from .models import City
from .serializers import CitySerializer


class CityViewSet(CustomMetaDataMixin, viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = [OAuth2Authentication, ]
