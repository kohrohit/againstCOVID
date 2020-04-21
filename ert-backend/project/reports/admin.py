from django.apps import apps
from django.contrib import admin

from reports.models import Report, UploadedFile

app = apps.get_app_config('reports')


class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'sid', 'details', 'is_prepared', 'prepared_at',)
    search_fields = ('id', 'sid',)


class UploadedFilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'report', 's3_url')
    search_fields = ('report__sid', 'report__id', 's3_url',)


for model_name, model in app.models.items():
    if model_name in ['report', 'uploadedfile',]:
        continue
    admin.site.register(model)

admin.site.register(Report, ReportAdmin)
admin.site.register(UploadedFile, UploadedFilesAdmin)
