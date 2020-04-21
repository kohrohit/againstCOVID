from rest_framework import serializers, generics
from . import models


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = ('id', 'name', 'icon', 'image', 'state', 'country', 'is_active', 'created_at')
        depth = 1
