from django.db import models

from .choices import RoleTypeChoices
from utilities.models import TimeStampMixin


class Executive(TimeStampMixin):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    role = models.CharField(max_length=4, choices=RoleTypeChoices.choices, validators=[RoleTypeChoices.validator])
    joined_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'executive'

    def __str__(self):
        return self.user
