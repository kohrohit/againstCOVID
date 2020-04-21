from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from utilities.models import TimeStampMixin


class ExecutiveLog(TimeStampMixin):
    created_by = models.ForeignKey("authentication.User",
                                   related_name='executive_log_created_by', on_delete=models.CASCADE)
    updated_by = models.ForeignKey("authentication.User",
                                   related_name='executive_log_updated_by', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    logged_object = GenericForeignKey('content_type', 'object_id')
    executive = models.ForeignKey('executives.Executive', on_delete=models.CASCADE)

    class Meta:
        app_label = 'logs'
        db_table = 'executive_log'

    def __str__(self):
        return '{} - {} - {}'.format(
            self.created_at,
            self.logged_object,
            str(self.executive.user)
        )

    @property
    def get_executive_name(self):
        return self.executive.user.first_name
