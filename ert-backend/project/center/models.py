from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.money import Money

from utilities.models import TimeStampMixin


class CustomCenterCluster(TimeStampMixin):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, null=True)

    class Meta:
        app_label = 'center'
        db_table = 'custom_center_cluster'

    def __str__(self):
        return self.name


class Center(TimeStampMixin):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    is_organization = models.BooleanField(default=False)
    organization = models.ForeignKey('authentication.Organization', null=True, blank=True, on_delete=models.SET_NULL)
    total_earnings = MoneyField(default=Money(0.0, 'INR'), max_digits=10, decimal_places=2, default_currency='INR')
    address = models.ForeignKey('authentication.Address', on_delete=models.PROTECT)
    comments = models.TextField(max_length=1000, default='')
    city = models.ForeignKey("operation_manifest.City", null=True, blank=True, on_delete=models.SET_NULL)
    custom_center_cluster = models.ManyToManyField('center.CustomCenterCluster', blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = 'center'
        db_table = 'center'

    def __str__(self):
        return self.name


class Branch(TimeStampMixin):
    center = models.ForeignKey('center.Center', on_delete=models.CASCADE)
    address = models.ForeignKey('authentication.Address', on_delete=models.PROTECT)
    city = models.ForeignKey("operation_manifest.City", null=True, blank=True, on_delete=models.SET_NULL)
    pin_code = models.CharField(max_length=10, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        app_label = 'center'
        db_table = 'branch'

    def __str__(self):
        return str(self.center)
