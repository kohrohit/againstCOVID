from django.contrib.gis.geos import Point
from django_filters.rest_framework import DjangoFilterBackend
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import filters, generics, mixins, viewsets, status
from rest_framework import permissions
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from authentication.choices import AddressTagChoices
from authentication.models import Address
from authentication.serializers import CreateUserSerializer
from miscellaneous.common_utils import get_state_instance_from_value
from miscellaneous.mixins import CustomMetaDataMixin
from operation_manifest.models import City, Country
from .models import Center, Branch
from .serializers import ListCenterSerializer, CenterMinimalListSerializer, \
    BranchMinimalListSerializer, CenterDetailSerializer


class ListAllCenterView(CustomMetaDataMixin, generics.ListAPIView):
    """
        Center App - This API is for list of all center data
    """
    queryset = Center.objects.all()
    serializer_class = ListCenterSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = [OAuth2Authentication, ]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['city',]
    search_fields = ['name',]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        if self.request.method == 'GET':
            return Center.objects.all()
        elif self.request.method == 'PATCH':
            return Center.objects.filter(pk=int(self.kwargs['pk']))
        else:
            return Center.objects.filter(user=self.request.user)


class CenterMinimalList(CustomMetaDataMixin, generics.ListAPIView):
    """
        Center App - This API is for list of center with minimal data
    """
    queryset = Center.objects.all()
    serializer_class = CenterMinimalListSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = [OAuth2Authentication, ]
    pagination_class = None


class CenterDetail(CustomMetaDataMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Center App - This API is for loading basic details for center
    """
    queryset = Center.objects.all()
    serializer_class = CenterDetailSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = [OAuth2Authentication, ]
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(user=user).first()
        return queryset

    def list(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()
        serializer = self.get_serializer(self.queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CenterBranchCreateView(CustomMetaDataMixin, generics.CreateAPIView, generics.ListAPIView):
    """
       SuperAdmin App - This API is for creating Center-Branch

       - This API creates a new Center and then Branch with same address
       - This Ensures that there will be at least one Branch object corresponding to one Center which
         cover's 95% of case.
       - Adding a new Branch to existing Center will be done in separate API
    """
    queryset = Center.objects.all()
    serializer_class = CenterMinimalListSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = [OAuth2Authentication, ]
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        driver = user.user_driver
        return self.queryset.get(id=driver.id)

    def list(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()
        serializer = self.get_serializer(self.queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        user_data = {
            'first_name': request.data['full_name'],
            'password': request.data['password'],
            'email': request.data['email'],
            'username': request.data['mobile']
        }
        user_serializer = CreateUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        # create a City Instance if not already in DB
        city_name = request.data['city_name']
        city_object = City.objects.filter(name__iexact=city_name)

        if city_object.exists():
            city_instance = city_object[0]
        else:
            country = Country.objects.get(id=1)  # id=1 will be INDIA
            state = request.data['state']
            state_object = get_state_instance_from_value(state)
            city_instance = City(name=city_name, country=country, state=state_object)
            city_instance.save()

        # create a Address instance
        # todo: currently this branch_name will go in name field of center and will be used to show branch name in frontend
        # todo: later we can add name field in branch Model also to handle the case of one-center multiple-branches
        branch_name = request.data['branch_name']
        address_name = 'PART:' + branch_name
        address_type = AddressTagChoices.OTHER
        branch_address = request.data['branch_address']
        branch_address_lat = request.data['branch_address_lat']
        branch_address_lon = request.data['branch_address_lon']
        geo_coordinates = Point(float(branch_address_lon), float(branch_address_lat))
        address_instance = Address(user=user, name=address_name, address_type=address_type, city=city_instance,
                                   geo_coordinates=geo_coordinates, address=branch_address)
        address_instance.save()

        # create a Center instance
        center = Center(name=branch_name, user=user, address=address_instance, city=city_instance)
        center.save()

        # create branch instance
        branch = Branch(center=center, address=address_instance, city=city_instance)
        branch.save()

        return Response('Center ' + branch_name + ' created successfully')


class ListBranchesForCenterView(CustomMetaDataMixin, generics.ListAPIView):
    """
    Center App - API to list all branches for center in order to update rate and density
    """
    queryset = Branch.objects.all()
    serializer_class = BranchMinimalListSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = [OAuth2Authentication, ]
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        center = user.center_set.first()
        center_branches = self.queryset.filter(center=center)
        return center_branches
