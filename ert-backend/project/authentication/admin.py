# from django.contrib import admin
# from authentication.models import User
#
#
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'email', 'is_staff', 'is_active')
#     list_filter = ['is_staff', 'is_active']
#     search_fields = ('id', 'email', 'mobile')
#     exclude = ['password']
#     readonly_fields = ['mobile', 'email', 'is_superuser', 'is_staff']
#     list_per_page = 20
#
# admin.site.register(User, UserAdmin)


from django.apps import apps
from django.contrib import admin
from .models import User, Address
app = apps.get_app_config('authentication')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'mobile', 'email', 'first_name')
    search_fields = ('id', 'mobile', 'email', 'first_name')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', )


for model_name, model in app.models.items():
    if model_name in ['user', 'address', ]:
        continue
    admin.site.register(model)

admin.site.register(User, UserAdmin)
admin.site.register(Address, AddressAdmin)
