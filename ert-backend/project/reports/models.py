from django.contrib.postgres.fields import JSONField
from django.db import models

from miscellaneous.common_utils import generate_nanoid
from utilities.models import TimeStampMixin


class Report(TimeStampMixin):
    sid = models.CharField(max_length=15, default=generate_nanoid)
    is_prepared = models.BooleanField(default=False)
    prepared_at = models.DateTimeField(blank=True, null=True)
    details = JSONField()

    class Meta:
        app_label = 'reports'
        db_table = 'reports'

    def __str__(self):
        return self.sid


class UploadedFile(TimeStampMixin):
    report = models.ForeignKey(Report, on_delete=models.PROTECT, editable=False)
    s3_url = models.TextField(max_length=50, editable=False)
    details = JSONField()

    class Meta:
        app_label = 'reports'
        db_table = 'uploaded_files'

    def __str__(self):
        return str(self.report.sid)
