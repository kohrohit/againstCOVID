from django.conf.urls import include, url
from rest_framework import routers
from .views import CenterMinimalList, ListAllCenterView, CenterBranchCreateView, ListBranchesForCenterView, CenterDetail

router = routers.DefaultRouter()
router.register(r'detail', CenterDetail)

urlpatterns = [
    url(r'', include((router.urls, 'center'))),
    url(r'^all/$', ListAllCenterView.as_view()),
    url(r'^minimal', CenterMinimalList.as_view()),
    url(r'^list_branches_for_center$', ListBranchesForCenterView.as_view()),
    # driver mobile app urls below
    url(r'^center_branch_create$', CenterBranchCreateView.as_view()),
]
