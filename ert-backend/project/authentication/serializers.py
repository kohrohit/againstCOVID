from oauth2_provider.models import AccessToken, RefreshToken
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from .exceptions import IncorrectOTPError, SignInViaOtpPNotAvailable
from .models import User, Organization, Staff


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'password', 'first_name', 'username', 'email', 'age', 'weight', 'height', 'gender')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = (
         'id', 'mobile', 'password', 'name', 'username', 'first_name', 'last_name', 'email', 'created_at', 'is_staff')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserMobileVerificationSerializer(serializers.ModelSerializer):
    mobile = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username',)

    def validate(self, attrs):
        get_object_or_404(User, username=attrs['username'])
        return attrs


class VerifyOTPSerializer(serializers.ModelSerializer):
    latest_otp = serializers.CharField(required=True, allow_blank=False, write_only=True)
    user_details = serializers.SerializerMethodField()
    access_token = serializers.SerializerMethodField()
    refresh_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('user_details', 'latest_otp', 'access_token', 'refresh_token',)

    def validate(self, attrs):
        print(attrs)
        user = self.context["user"]
        latest_otp = attrs['latest_otp']

        try:
            user.verify_otp(latest_otp)
        except IncorrectOTPError as e:
            raise IncorrectOTPError
            # raise serializers.ValidationError(detail={'latest_otp': str(e)})

        user.latest_otp = ''
        user.save()
        return user

    def get_user_details(self, user):
        return {
            "id": user.id,
            "mobile": user.mobile,
            "name": "",
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "created_at": user.created_at,
        }

    def get_access_token(self, user):
        try:
            return user.get_access_token()
        except SignInViaOtpPNotAvailable as e:
            raise serializers.ValidationError(detail={'user': str(e)})
        except AccessToken.DoesNotExist:
            raise serializers.ValidationError(detail={'user': str(SignInViaOtpPNotAvailable())})

    def get_refresh_token(self, user):
        try:
            return user.get_refresh_token()
        except SignInViaOtpPNotAvailable as e:
            raise serializers.ValidationError(detail={'user': str(e)})
        except RefreshToken.DoesNotExist:
            raise serializers.ValidationError(detail={'user': str(SignInViaOtpPNotAvailable())})


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

    def validate(self, attrs):
        if Staff.objects.filter(user=attrs['user']).exists():
            raise serializers.ValidationError(
                detail={"staff_exists": "Entered user is a previously created staff"}
            )

        return attrs
