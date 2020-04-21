from rest_framework import serializers
from .models import Center, Branch


class ListCenterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    owned_by = serializers.SerializerMethodField()
    branches = serializers.SerializerMethodField()
    mobile = serializers.CharField(source='user.mobile', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    city_name = serializers.CharField(source='city.name', default='-', read_only=True)

    def get_owned_by(self, obj):
        full_name = '%s %s' % (obj.user.first_name, obj.user.last_name)
        return full_name.strip().upper()

    def get_branches(self, partner_obj):
        all_branches = partner_obj.branch_set.all()
        branches_data = []
        if all_branches.exists():
            for single_branch in all_branches:
                branch_lat_lon = single_branch.address.geo_coordinates.coords
                branches_data.append({
                    'branch_id': single_branch.id,
                    'branch_name': partner_obj.name,
                    'branch_address': single_branch.address.address,
                    'branch_lat_lon': {
                        'lat': branch_lat_lon[1],
                        'lon': branch_lat_lon[0],
                    }
                })
        return branches_data

    class Meta:
        model = Center
        fields = ('id', 'name', 'username', 'mobile', 'email', 'total_earnings',
                  'city_name', 'owned_by', 'branches')
        depth = 1


class CenterMinimalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = ('id', 'name')


class CenterDetailSerializer(serializers.ModelSerializer):
    """
    - This Serializer is for loading center's basic details in App
    - currently assuming that every center has one branch the rate,density,address,lat,lon are sent from the first branch
    """
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    mobile = serializers.CharField(source='user.mobile', read_only=True)
    address = serializers.SerializerMethodField()
    stationary_lat = serializers.SerializerMethodField()
    stationary_lon = serializers.SerializerMethodField()

    class Meta:
        model = Center
        fields = ('id', 'name', 'first_name', 'last_name', 'email', 'mobile', 'address', 'stationary_lat',
                  'stationary_lon')

    def get_address(self, partner):
        branch = partner.branch_set.first()
        if branch.address is not None:
            return branch.address.address
        else:
            return '-'

    def get_stationary_lat(self, partner):
        branch = partner.branch_set.first()
        if branch.address is not None:
            branch_coordinates = branch.address.geo_coordinates.coords
            return branch_coordinates[1]
        else:
            print('Invalid Branch coordinates!!')
            return None

    def get_stationary_lon(self, partner):
        branch = partner.branch_set.first()
        if branch.address is not None:
            branch_coordinates = branch.address.geo_coordinates.coords
            return branch_coordinates[0]
        else:
            print('Invalid Branch coordinates!!')
            return None


class BranchMinimalListSerializer(serializers.ModelSerializer):
    branch_name = serializers.CharField(source='center.name')

    class Meta:
        model = Branch
        fields = ('id', 'branch_name')


class CenterBranchCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Center
        fields = ('name', 'user')
