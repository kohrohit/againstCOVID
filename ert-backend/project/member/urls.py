from django.conf.urls import include, url
from rest_framework import routers

from member import views
from .views import UpdateProfile, MemberDetailView

router = routers.DefaultRouter()
router.register(r'all', views.MemberViewSet)

urlpatterns = [
    url(r'', include((router.urls, 'member'))),
    url(r'^detail$', MemberDetailView.as_view()),
    url(r'^update/profile$', UpdateProfile.as_view()),
]
