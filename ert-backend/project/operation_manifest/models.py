from django.db import models
from utilities.models import TimeStampMixin, AddressMixin
from .choices import IndianStateChoices, CurrencyChoices


class Country(TimeStampMixin):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = "operation_manifest"
        db_table = 'country'

    def __str__(self):
        return self.name


class IndianState(TimeStampMixin):
    name = models.CharField(max_length=3, choices=IndianStateChoices.choices, validators=[IndianStateChoices.validator])
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = "operation_manifest"
        db_table = 'indian_state'

    def __str__(self):
        return self.name


class City(TimeStampMixin, AddressMixin):
    name = models.CharField(max_length=50, unique=True)
    icon = models.URLField(blank=True, null=True, max_length=120)
    image = models.URLField(blank=True, null=True, max_length=120)
    state = models.ForeignKey("IndianState", on_delete=models.CASCADE)
    country = models.ForeignKey("Country", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = "operation_manifest"
        db_table = 'city'

    def __str__(self):
        return self.name


class Forex(TimeStampMixin):
    currency = models.CharField(max_length=3, choices=CurrencyChoices.choices, default=CurrencyChoices.USD,
                                validators=[CurrencyChoices.validator])
    inr_rate = models.FloatField()

    class Meta:
        app_label = 'operation_manifest'
        db_table = 'forex'

    def __str__(self):
        return str(self.currency) + " " + str(round(self.inr_rate, 2))


class DailyLimit(TimeStampMixin):
    count = models.IntegerField()

    class Meta:
        app_label = 'operation_manifest'
        db_table = 'daily_limit'

    def __str__(self):
        return str(self.count)

