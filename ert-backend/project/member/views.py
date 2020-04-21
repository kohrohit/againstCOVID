from django_filters.rest_framework import DjangoFilterBackend
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import generics, status, filters, viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from authentication.models import User
from miscellaneous.logging_utils import show_error
from miscellaneous.mixins import CustomMetaDataMixin
from .filters import MemberFilter
from .models import Member
from .serializers import MemberSerializer, UpdateProfileSerializer, MemberDetailSerializer


class MemberViewSet(CustomMetaDataMixin, viewsets.ModelViewSet):
    """
    Super Admin App - This ViewSet is for loading all members with filtering and searching
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = [OAuth2Authentication, ]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = MemberFilter
    search_fields = ['name']
    pagination_class = LimitOffsetPagination


class MemberDetailView(CustomMetaDataMixin, generics.ListAPIView):
    """
        Member App - This API is for list of member with minimal data
    """
    queryset = Member.objects.all()
    serializer_class = MemberDetailSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = [OAuth2Authentication, ]
    pagination_class = None

    # todo: use get_object instead
    def get_object(self):
        obj = Member.objects.get(user=self.request.user)
        return obj

    def list(self, request, *args, **kwargs):
        member_obj = self.get_object()
        serializer = self.get_serializer(member_obj)
        return Response(serializer.data)


class UpdateProfile(CustomMetaDataMixin, generics.CreateAPIView):
    """
        Member App - This API to update user profile
    """
    queryset = User.objects.all()
    serializer_class = UpdateProfileSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = [OAuth2Authentication, ]
    pagination_class = None

    def perform_update(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        try:
            if 'user_id' in request.data:
                user_data = User.objects.get(id=request.data['user_id'])
                serializer = self.get_serializer(user_data, data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                return Response('member profile updated successfully')
        except Exception as e:
            show_error(e)
            print(e)
            return Response("something went wrong", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

