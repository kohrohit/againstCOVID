from django.apps import apps
from django.contrib import admin

from .models import Center, Branch

app = apps.get_app_config('center')


class CenterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'is_active')
    search_fields = ('name', 'id',)


class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'center', 'is_active')
    search_fields = ('center__name', 'id',)


for model_name, model in app.models.items():
    if model_name in ['center', 'branch', ]:
        continue
    admin.site.register(model)

admin.site.register(Center, CenterAdmin)
admin.site.register(Branch, BranchAdmin)
