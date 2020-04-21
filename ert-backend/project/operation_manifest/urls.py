from django.conf.urls import include, url
from rest_framework import routers

from operation_manifest import views

router = routers.DefaultRouter()
router.register(r'all', views.CityViewSet)


urlpatterns = [
    url(r'', include((router.urls, 'city'), namespace='city')),
]
