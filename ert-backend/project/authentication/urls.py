from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers

from authentication.views import MemberLogin, MemberSignup, \
    MemberCheckUsernameEmailMobile, ForgotPasswordMail, SendSignUpOtp, VerifySignupOtp
from authentication.views import SendLoginOtp, user_reset_password_verify, user_reset_password_render, get_fcm_token
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'login-via-otp', views.UserOTPViewSet)

urlpatterns = [
    url(r'', include((router.urls, 'authentication'), namespace='authentication')),
    path('register/', views.register),
    path('get/refresh/token', views.refresh_token),
    url(r'^member/login$', MemberLogin.as_view()),
    url(r'^member/login/otp$', SendLoginOtp.as_view()),
    url(r'^member/signup$', MemberSignup.as_view()),
    url(r'^member/check/username/email/mobile$', MemberCheckUsernameEmailMobile.as_view()),
    url(r'^member/forgot/password$', ForgotPasswordMail.as_view()),
    url(r'^member/send/signup/otp$', SendSignUpOtp.as_view()),
    url(r'^member/verify/signup/otp$', VerifySignupOtp.as_view()),
    url(r'^member/user_reset_password$', user_reset_password_render, name='user_reset_password_render'),
    url(r'^member/user_reset_password_process$', user_reset_password_verify, name='user_reset_password_verify'),
    url(r'^fcm_token', get_fcm_token),
]
