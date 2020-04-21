from rest_framework import status
from rest_framework.exceptions import APIException


class IncorrectOTPError(APIException):
    custom_code = 1750
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "The provided otp is incorrect. Please check carefully and try again"


class InvalidAccessTokenError(APIException):
    custom_code = 1500
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'The access token is invalid.'


class SignInViaOtpPNotAvailable(APIException):
    custom_code = 2000
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'This sign-in method is not available for the user.'
