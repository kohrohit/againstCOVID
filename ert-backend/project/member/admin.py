from django.contrib import admin
from django.apps import apps

from .models import Member
app = apps.get_app_config('member')


class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('name', 'user__mobile', 'user__email')


for model_name, model in app.models.items():
    if model_name in ['member', 'memberasset']:
        continue
    admin.site.register(model)

admin.site.register(Member, MemberAdmin)
