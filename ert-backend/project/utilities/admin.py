from django.contrib import admin
from django.apps import apps
from django_fsm_log.admin import StateLogInline
from django_fsm_log.models import StateLog

app = apps.get_app_config('utilities')

for model_name, model in app.models.items():
    admin.site.register(model)


@admin.register(StateLog)
class FSMModelAdmin(admin.ModelAdmin):
    inlines = [StateLogInline]
