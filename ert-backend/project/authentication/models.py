from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.gis.db.models import PointField
from django.core.validators import RegexValidator
from django.db import models

from executives.choices import RoleTypeChoices
from utilities.models import TimeStampMixin, AddressMixin
from .choices import AddressTagChoices, KYCDocumentTypeChoices, OrganizationTypeChoices
from .exceptions import IncorrectOTPError, InvalidAccessTokenError, SignInViaOtpPNotAvailable


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given username, mobile and password.
        """

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, null=True, max_length=60)
    name = models.CharField(max_length=60)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    mobile = models.CharField(max_length=13, null=True, blank=True, validators=[RegexValidator(regex="^\d{10}$")])
    latest_otp = models.CharField(max_length=6, null=True, blank=True)
    type = models.CharField(max_length=5)
    age = models.CharField(max_length=5, null=True)
    weight = models.CharField(max_length=5, null=True)
    height = models.CharField(max_length=5, null=True)
    gender = models.CharField(max_length=5, null=True)
    activation_code = models.CharField(max_length=200, null=True, blank=True)
    image_url = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    fcm_token = models.CharField(max_length=200, blank=True, null=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        app_label = 'authentication'
        db_table = 'user'

    def __str__(self):
        return str(self.first_name) + ": " + str(self.username)

    def verify_otp(self, latest_otp: str):
        if latest_otp == "" or latest_otp != self.latest_otp:
            raise IncorrectOTPError()
        return True

    def verify_access_token(self, token: str):
        token_obj = self.oauth2_provider_accesstoken.filter(token=token).latest('id')
        if token_obj:
            if token_obj.is_valid():
                return True
            raise InvalidAccessTokenError()

    _token_obj = None

    def get_access_token(self):
        self._token_obj = self.oauth2_provider_accesstoken.filter(user=self.id).latest('id')
        if self._token_obj:
            if self._token_obj.is_valid():
                return self._token_obj.token
        raise SignInViaOtpPNotAvailable()

    def get_refresh_token(self):
        if self._token_obj is not None:
            if self._token_obj.is_valid():
                return self._token_obj.refresh_token.token
            else:
                raise SignInViaOtpPNotAvailable()
        else:
            refresh_token_obj = self.oauth2_provider_refreshtoken.filter(user=self.id).latest('id')
            if refresh_token_obj:
                if refresh_token_obj.is_valid():
                    return refresh_token_obj.token
            raise SignInViaOtpPNotAvailable()


class Staff(TimeStampMixin):
    user = models.ForeignKey('User', on_delete=models.PROTECT)
    role = models.CharField(max_length=5, choices=RoleTypeChoices.choices, validators=[RoleTypeChoices.validator])
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = 'authentication'
        db_table = 'staff'

    def __str__(self):
        return str(self.user)


class Organization(TimeStampMixin):
    name = models.CharField(max_length=60)
    owner = models.ForeignKey('User', related_name='organization_owner', on_delete=models.PROTECT)
    staff = models.ManyToManyField("authentication.Staff", through="authentication.OrganizationStaffMapping",
                                   blank=True)
    type = models.CharField(max_length=4, choices=OrganizationTypeChoices.choices,
                            validators=[OrganizationTypeChoices.validator])
    pan = models.CharField(null=True, blank=True, max_length=128)
    pan_image_url = models.CharField(max_length=200, null=True, blank=True)
    gstin = models.CharField(null=True, blank=True, max_length=30)
    secondary_mobile_number = models.CharField(max_length=13, validators=[RegexValidator(regex="^\d{10}$")], null=True,
                                               blank=True)
    accounts_mobile_number = models.CharField(max_length=13, validators=[RegexValidator(regex="^\d{10}$")], null=True,
                                              blank=True)
    accounts_email = models.EmailField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = 'authentication'
        db_table = 'organization'

    def __str__(self):
        return self.name

    def add_staff_member(self, staff_obj):
        OrganizationStaffMapping.objects.get_or_create(organization=self, staff=staff_obj)


class OrganizationStaffMapping(TimeStampMixin):
    organization = models.ForeignKey("authentication.Organization", on_delete=models.CASCADE)
    staff = models.ForeignKey("authentication.Staff", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = 'authentication'
        unique_together = ['organization', 'staff']
        db_table = 'organization_staff_mapping'

    def __str__(self):
        return 'Organization: {0} & Staff: {1}'.format(str(self.organization_id), str(self.staff_id))


class Address(AddressMixin, TimeStampMixin):
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=40)
    tag = models.ForeignKey('utilities.Tag', null=True, blank=True, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=5, default=AddressTagChoices.OTHER, choices=AddressTagChoices.choices,
                                    validators=[AddressTagChoices.validator])
    contact_person_phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    city = models.ForeignKey("operation_manifest.City", related_name='address_city', null=True, blank=True,
                             on_delete=models.SET_NULL)
    is_default = models.BooleanField(default=False)

    class Meta:
        app_label = 'authentication'
        db_table = 'address'

    def __str__(self):
        return str(self.id) + ': ' + str(self.name)


class KYCDocument(TimeStampMixin):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    identification_proof_type = models.CharField(max_length=5, choices=KYCDocumentTypeChoices.choices,
                                                 validators=[KYCDocumentTypeChoices.validator])
    unique_number = models.CharField(max_length=128)
    front_image_url = models.CharField(max_length=200, null=True, blank=True)
    back_image_url = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = 'authentication'
        db_table = 'kyc_document'

    def __str__(self):
        return str(self.user) + ": " + self.identification_proof_type
