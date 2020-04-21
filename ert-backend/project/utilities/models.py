from django.contrib.gis.db.models import PointField
from django.db import models

from .choices import PlatformChoices, TagChoices


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AddressMixin(models.Model):
    """
        To Store the place_id by google API
    """
    place_id = models.CharField(max_length=200, blank=True)
    geo_coordinates = PointField(null=True, blank=True,)
    pin_code = models.CharField(max_length=10, blank=True)
    address = models.TextField(max_length=300, blank=True)
    landmark = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class Platform(models.Model):
    name = models.CharField(max_length=10, choices=PlatformChoices.choices, validators=[PlatformChoices.validator])
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = "utilities"
        db_table = 'platform'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=5, choices=TagChoices.choices,
                            null=True, blank=True, validators=[TagChoices.validator])
    description = models.TextField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = "utilities"
        db_table = 'tag'

    def __str__(self):
        return self.name
