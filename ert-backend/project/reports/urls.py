from django.conf.urls import include, url
from rest_framework import routers
from .views import generate_report, ListAllReportView, GetReportView

router = routers.DefaultRouter()

urlpatterns = [
    url(r'', include((router.urls, 'reports'))),
    url(r'^generate$', generate_report),
    url(r'^list$', ListAllReportView.as_view()),
    url(r'^get$', GetReportView.as_view()),
]
