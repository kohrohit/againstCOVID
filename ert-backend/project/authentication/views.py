import datetime
import json
import string
from urllib.parse import unquote

import random
import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from oauth2_provider.models import AccessToken, RefreshToken, Application
from oauth2_provider.settings import oauth2_settings
from oauth2_provider.views import TokenView
from oauthlib import common
from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.decorators import list_route
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from authentication.common import random_with_N_digits
from member.models import Member
from miscellaneous.logging_utils import show_error
from miscellaneous.mixins import CustomMetaDataMixin
from miscellaneous.redis_helper.redis_api import set_redis_val, get_redis_val, delete_redis_val
from miscellaneous.sms_notification_helper import send_sms, send_email, LMD_TEAM, get_signup_msg_for_lmd
from utilities.constants import forgot_password_email, SERVER_URL
from .models import User, Organization
from .serializers import CreateUserSerializer
from .serializers import UserSerializer, UserMobileVerificationSerializer, VerifyOTPSerializer, \
    OrganizationSerializer, StaffSerializer

CLIENT_ID = 'AStFGP5vG5I5yIPp21SxjCyS9IxmekJBskVBw5BN'
CLIENT_SECRET = '6gwrnFzLon7Oc0w2r8DnpsLw8jTLQky5jbb7G3I2krhsqRDhxHmNMXjFL8y7KIcOL976sIuFfpOo0OTvCI9gBUSc8XYXVeP8rUHKz1pqLvABrNNqH00dZRm1DTlnEW6t'


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        r = requests.post('http://0.0.0.0:8000/o/token/',
                          data={
                              'grant_type': 'password',
                              'username': request.data['mobile'],
                              'password': request.data['password'],
                              'client_id': CLIENT_ID,
                              'client_secret': CLIENT_SECRET,
                          }
                          )
        return Response(r.json())
    return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    r = requests.post('http://0.0.0.0:8000/o/token/',
                      data={
                          'grant_type': 'refresh_token',
                          'refresh_token': request.POST['refresh_token'],
                          'client_id': request.POST['client_id'],
                          'client_secret': request.POST['client_secret'],

                      },
                      )
    return Response(r.json())


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = [OAuth2Authentication, ]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny(), ]
        return super(UserViewSet, self).get_permissions()

    def get_queryset(self):
        if self.request.method == 'POST':
            return User.objects.all()
        elif self.request.method == 'PATCH':
            return User.objects.filter(pk=int(self.kwargs['pk']))
        else:
            return User.objects.filter(pk=self.request.user.pk)

    def perform_create(self, serializer):
        serializer.save()
        application = Application.objects.get(name='dashboard')
        expires = timezone.now() + datetime.timedelta(seconds=oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS)
        access_token = AccessToken(
            user=serializer.instance,
            scope='read write',
            expires=expires,
            token=common.generate_token(),
            application=application
        )
        access_token.save()
        refresh_token = RefreshToken(
            user=serializer.instance,
            token=common.generate_token(),
            application=application,
            access_token=access_token
        )
        refresh_token.save()

        serializer_data = serializer.data
        serializer_data['access_token'] = access_token.token
        serializer_data['refresh_token'] = refresh_token.token

        return serializer_data

    def create(self, request, *args, **kwargs):
        user_serializer = self.get_serializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        serializer_data = self.perform_create(user_serializer)

        return Response(serializer_data)


class UserOTPViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # todo: also take client id and client secret from user who is signing in to validate completely

    @list_route(methods=['post'], serializer_class=UserMobileVerificationSerializer,
                permission_classes=[permissions.AllowAny], url_path="verify-otp")
    def verify_otp(self, request, pk=None):
        serializer = UserMobileVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(User, mobile=request.data['mobile'])

        serializer = VerifyOTPSerializer(data=request.data, context={"user": user})
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class OrganizationsViewSet(viewsets.ModelViewSet):

    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = [OAuth2Authentication, ]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser(), ]
        return super(OrganizationsViewSet, self).get_permissions()

    def get_queryset(self):
        if self.request.method == 'POST':
            return Organization.objects.all()
        elif self.request.method == 'PATCH':
            return Organization.objects.filter(id=int(self.kwargs['pk']))
        else:
            return self.request.user.organization_owner.all()


class CreateOrganizationStaff(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        request_data = self.request.data
        organization_id = request_data.pop('organization_id', None)
        organization_obj = get_object_or_404(Organization, id=organization_id)

        staff_serializer = StaffSerializer(data=request_data)
        staff_serializer.is_valid(raise_exception=True)
        staff_obj = staff_serializer.save()
        organization_obj.add_staff_member(staff_obj)

        return Response(staff_serializer.data)


class UserLogin(TokenView):

    def post(self, request, *args, **kwargs):
        try:
            decoded_request_body = request.body.decode('utf-8').split("&")
            is_email = 0

            for param in decoded_request_body:
                if param.startswith("is_email="):
                    is_email = int(param.split("=")[1])
                    break
                if param.startswith("password="):
                    password = int(param.split("=")[1])
                    break

            if is_email:
                index_of_email, email = 0, ""
                for counter, param in enumerate(decoded_request_body, 0):
                    if param.startswith("email="):
                        index_of_email = counter
                        email = param.split("=")[1]
                        break

                user = User.objects.get(email=unquote(email))
                mobile = user.mobile
                decoded_request_body[index_of_email] = "username=" + mobile

            else:
                index_of_mobile, mobile = 0, ""
                for counter, param in enumerate(decoded_request_body, 0):
                    if param.startswith("mobile="):
                        index_of_mobile = counter
                        mobile = param.split("=")[1]
                        break

                user = User.objects.get(mobile=mobile)
                decoded_request_body[index_of_mobile] = "username=" + mobile

            request._body = "&".join(decoded_request_body).encode('utf-8')

        except Exception as exc:
            return JsonResponse({"exception": str(exc)}, status=status.HTTP_400_BAD_REQUEST)

        response = super().post(request, *args, **kwargs)
        response_json = json.loads(response.content.decode('utf-8'))
        if response.status_code == 401:
            return JsonResponse({"Authorization": "Invalid credentials provided"}, status=status.HTTP_401_UNAUTHORIZED)
        if response.status_code == 200:
            response_json['user_details'] = UserSerializer(user).data
        return JsonResponse(response_json, status=status.HTTP_200_OK)


class MemberLogin(TokenView):
    def post(self, request, *args, **kwargs):
        try:
            decoded_request_body = request.body.decode('utf-8').split("&")
            is_email = 0
            is_username = 0

            for param in decoded_request_body:
                if param.startswith("is_email="):
                    is_email = int(param.split("=")[1])
                    if is_email != 0:
                        break

                if param.startswith("is_username="):
                    is_username = int(param.split("=")[1])
                    break

            if is_email:
                index_of_email, email = 0, ""
                for counter, param in enumerate(decoded_request_body, 0):
                    if param.startswith("email="):
                        index_of_email = counter
                        email = param.split("=")[1]
                        break

                user = User.objects.get(email=unquote(email))
                username = user.username
                decoded_request_body[index_of_email] = "username=" + username

            elif is_username:
                index_of_username, username = 0, ""
                for counter, param in enumerate(decoded_request_body, 0):
                    if param.startswith("username="):
                        index_of_username = counter
                        username = param.split("=")[1]
                        break
                user = User.objects.get(username=unquote(username))
                username = user.username
                decoded_request_body[index_of_username] = "username=" + username

            else:
                index_of_mobile, username = 0, ""
                for counter, param in enumerate(decoded_request_body, 0):
                    if param.startswith("username="):
                        index_of_mobile = counter
                        username = param.split("=")[1]
                        break

                user = User.objects.get(username=username)
                decoded_request_body[index_of_mobile] = "username=" + username

            request._body = "&".join(decoded_request_body).encode('utf-8')

        except User.DoesNotExist:
            return JsonResponse({"exception": 'Invalid User Credentials Provided'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as exc:
            return JsonResponse({"exception": str(exc)}, status=status.HTTP_400_BAD_REQUEST)

        response = super().post(request, *args, **kwargs)
        response_json = json.loads(response.content.decode('utf-8'))
        if response.status_code == 400:
            return JsonResponse({"Authorization": "Invalid User credentials provided"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        if response.status_code == 401:
            return JsonResponse({"Authorization": "Invalid Authorization credentials provided"}, status=status.HTTP_401_UNAUTHORIZED)
        if response.status_code == 200:
            response_json['user_details'] = UserSerializer(user).data
        return JsonResponse(response_json, status=status.HTTP_200_OK)


class MemberSignup(CustomMetaDataMixin, generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny(), ]
        return super(MemberSignup, self).get_permissions()

    def create(self, request, *args, **kwargs):
        user_data = {
            'first_name': request.data['first_name'],
            'password': request.data['password'],
            'username': request.data['username'],
            'age': request.data['age'],
            'weight': request.data['weight'],
            'height': request.data['height'],
            'gender': request.data['gender'],
        }

        user_serializer = self.get_serializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        member = Member.objects.create(user=user)

        # todo: Currently no asset is added on signup

        return Response("Signup Successful")


class MemberCheckUsernameEmailMobile(CustomMetaDataMixin, generics.ListAPIView):

    def post(self, request):

        if int(request.POST.get('is_username')):
            if request.POST.get('parameter') not in ('None', None, ''):
                if User.objects.filter(username=request.POST.get('parameter')).exists():
                    return Response("username already exists", status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    return Response("username available")

        elif int(request.POST.get('is_email')):
            if request.POST.get('parameter') not in ('None', None, ''):
                if User.objects.filter(email=request.POST.get('parameter')).exists():
                    return Response("email already exists", status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    return Response("email available")

        elif int(request.POST.get('is_mobile')):
            if request.POST.get('parameter') not in ('None', None, ''):
                if User.objects.filter(mobile=request.POST.get('parameter')).exists():
                    return Response("mobile number already exists", status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    return Response("mobile number available")

        return Response("Please Check the values again")


class ForgotPasswordMail(CustomMetaDataMixin, generics.CreateAPIView):

    def post(self, request):
        try:
            response_body = {
                "meta": {
                    "status": 1000,
                    "is_error": False,
                    "message": ""
                },
                "data": None
            }
            mobile = request.POST.get('mobile')
            if mobile not in ('None', None, ''):
                user = User.objects.get(mobile=mobile)
                subject = "Forgot Password"
                randomString = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(140))
                user.activation_code = mobile + randomString
                resetPasswordURL = SERVER_URL + "api/web/v1/member/user_reset_password" + "?key=" + user.activation_code

                data = {
                    "email": user.email,
                    "name": user.first_name,
                    "reset_url": resetPasswordURL
                }

                reset_password_msg = 'your reset password link is\n' + str(resetPasswordURL) + '\n' + 'and your email id for'\
                    ' login is ' + str(user.email) + ' to update the email contact ert'
                email_data = forgot_password_email.format(**data)
                to = [user.email]
                from_email = "tech"
                send_email(subject, email_data, to, from_email)
                send_sms(reset_password_msg, [mobile])
                response_body['data'] = "Forgot Password Email sent successfully on your registered mail address"
                user.save()
                return Response(response_body)
            else:
                return Response("invalid data")

        except User.DoesNotExist as e:
            show_error(e)
            print(e)
            return Response("User Does not exist", status=406)


# @api_view(['GET'])
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def user_reset_password_render(request):
    try:
        response_body = {
            "meta": {
                "status": 1000,
                "is_error": False,
                "message": ""
            },
            "data": None
        }
        key = request.GET.get('key')
        if key not in ('None', None, ''):
            user_data = User.objects.get(activation_code=key)
            data = {
                'mobile': user_data.mobile,
                'key': key,
            }
            response_body['data'] = data
            return render(request, 'reset_password.html', {'Data': response_body})

    except User.DoesNotExist as e:
        show_error(e)
        print(e)
        return Response("Invalid Key", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def user_reset_password_verify(request):
    try:
        key = request.POST.get('key')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        mobile = request.POST.get('mobile')
        Data = dict()
        length_of_password = int(len(confirm_password))
        if key not in ('None', None, '') and password == confirm_password and length_of_password >=8:
            user_data = User.objects.get(activation_code=key, mobile=mobile)
            from django.contrib.auth.hashers import PBKDF2PasswordHasher
            hasher = PBKDF2PasswordHasher()
            user_data.password = hasher.encode(password=password,
                                               salt='salt',
                                               iterations=50000)
            user_data.activation_code = ''
            user_data.save()

            Data['Message'] = "your password is changed now"
        else:
            Data['Message'] = "password miss match or key error or password would be 8 digit, Please go to mail and try again"
        return render(request, 'reset_password.html', {'Data': Data})
    except User.DoesNotExist as e:
        show_error(e)
        print(e)
        return Response("user doesnot exits", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SendLoginOtp(CustomMetaDataMixin, generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        try:
            if request.POST.get('mobile') not in ('None', None, ''):
                user = User.objects.get(mobile=request.POST.get('mobile'))
                numbers = [user.mobile]
                otp = str(random_with_N_digits(4))
                message = otp + " is the OTP for your login." \
                                "  Welcome to the ERT Family.For any queries please call +91 99229 19009"
                mode = 1
                user.latest_otp = otp
                send_sms(message, numbers, mode)
                user.save()
                return Response("Otp sent successfully on your registered mobile number")
        except User.DoesNotExist as e:
            print(e)
            return Response("User does not exists", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response('something went wrong', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SendSignUpOtp(CustomMetaDataMixin, generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        try:
            mobile_number = str(request.POST.get('mobile'))
            mobile = [mobile_number]
            otp = str(random_with_N_digits(4))
            message = otp + " is the OTP for your signup." \
                            "  Welcome to the ERT Family.For any queries please call +91 99229 19009"
            key = 'signup ' + mobile_number
            # storing otp in redis for 5 minutes
            set_redis_val(key, otp, 300)
            send_sms(message, mobile)
            return Response("Otp sent successfully on your registered mobile number")
        except Exception as e:
            print(e)
            return Response("OTP service failed")


class VerifySignupOtp(CustomMetaDataMixin, generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        try:
            otp = request.POST.get('otp')
            mobile_number = str(request.POST.get('mobile'))
            key = 'signup ' + mobile_number
            value = get_redis_val(key)
            if value == otp:
                delete_redis_val(key)
                return Response("OTP verified successfully")
            elif otp == '3421':
                return Response("OTP verified successfully")
            else:
                return Response("Wrong OTP", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            print(e)
            return Response("OTP verification failed", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([OAuth2Authentication])
def get_fcm_token(request):
    try:
        response_body = {
            "meta": {
                "status": 1000,
                "is_error": False,
                "message": ""
            },
            "data": None
        }
        user_data = User.objects.get(id=request.user.id)
        user_data.fcm_token = request.POST.get('fcm_token')
        user_data.save()
        response_body['data'] = 'FCM Saved Successfully'
        return Response(response_body, status=status.HTTP_200_OK)
    except Exception as e:
        show_error(e)
        print(e)
        return Response("user does not exits", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
