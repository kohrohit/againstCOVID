from datetime import datetime

from django.db import models

from utilities.models import TimeStampMixin


class Member(TimeStampMixin):
    user = models.OneToOneField('authentication.User', on_delete=models.CASCADE)
    is_organization = models.BooleanField(default=False)
    organization = models.ForeignKey('authentication.Organization', null=True, blank=True, on_delete=models.CASCADE)
    address = models.ForeignKey('authentication.Address', null=True, blank=True, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = 'member'
        db_table = 'member'

    def __str__(self):
        return str(self.user.username)

    def generate_daily_otp(self):
        self.daily_otp = get_4_digit_random_number()
        self.daily_otp_generated_at = datetime.now()
