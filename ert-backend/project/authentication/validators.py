from oauth2_provider.oauth2_validators import OAuth2Validator
from django.contrib.auth import get_user_model
USER_MODEL = get_user_model()


class CustomOAuth2Validator(OAuth2Validator):  # pylint: disable=w0223
    """ Primarily extend the functionality of token generation """

    def validate_user(self, username, password, client, request, *args, **kwargs):
        """ Here, you would be able to access the MOBILE/ OTP fields
            which you will be sending in the request.post body. """
        if hasattr(request, 'is_otp'):
            if request.is_otp in (1, '1'):
                otp = request.otp
                username = request.username
                try:
                    user = USER_MODEL.objects.get(latest_otp=otp, username=username)
                except USER_MODEL.DoesNotExist:
                    return False
                if user is not None and user.is_active:
                    request.user = user
                    return True
                return False
            else:
                return super().validate_user(username, password, client, request, *args, **kwargs)
        else:
            return super().validate_user(username, password, client, request, *args, **kwargs)
