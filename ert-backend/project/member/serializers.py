from rest_framework import serializers

from authentication.models import User
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    contact_number = serializers.CharField(source='user.mobile')
    email = serializers.CharField(source='user.email')
    name = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = ('id', 'name', 'contact_number', 'email', 'is_active')
        depth = 0

    def get_name(self, member_obj):
        return member_obj.user.first_name + " " + member_obj.user.last_name


class MemberDetailSerializer(serializers.ModelSerializer):
    member_id = serializers.IntegerField(source='id')
    user_id = serializers.IntegerField(source='user.id')
    mobile = serializers.CharField(source='user.mobile')
    email = serializers.CharField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    support_email = serializers.SerializerMethodField()
    support_mobile = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = ('member_id', 'user_id', 'mobile', 'email', 'first_name', 'support_email', 'support_mobile')

    def get_support_email(self, instance):
        return 'membercare@ert.com'

    def get_support_mobile(self, instance):
        return '+919900990099'


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name')

