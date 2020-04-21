from django.conf.urls import include, url
from rest_framework import routers

from .views import ContentTypeViewSet, ChoicesFullFormsView, TransitionMapAPIView

router = routers.DefaultRouter()
router.register(r'content-type', ContentTypeViewSet)

urlpatterns = [
    url(r'', include((router.urls, 'utilities'), namespace='utilities')),
    url(r'^choices-full-forms', ChoicesFullFormsView.as_view(), name='get_choices_full_forms'),
    url(r'^transition-map/', TransitionMapAPIView.as_view()),
]
