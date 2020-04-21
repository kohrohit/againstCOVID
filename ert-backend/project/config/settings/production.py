from .base import *

# AWS S3 settings for static files

AWS_STORAGE_BUCKET_NAME = 'drf-static'
AWS_S3_REGION_NAME = 'ap-south-1'
AWS_ACCESS_KEY_ID = get_secret("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = get_secret('AWS_SECRET_ACCESS_KEY')
# Tell django-storages the domain to use to refer to static files
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_LOCATION = 'static'
AWS_DEFAULT_ACL = None


# Tell the staticfiles app to use S3Boto3 storage when writing the collected static files (when
# you run `collectstatic`).
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': get_secret("DATABASE_NAME"),
        'USER': get_secret("DATABASE_USER"),
        'PASSWORD': get_secret("DATABASE_PASSWORD"),
        'HOST': get_secret("DATABASE_HOST"),
        'PORT': get_secret("DATABASE_PORT"),
    }
}

# REDIS Settings

REDIS_CONFIG = {
    'HOST': get_secret("REDIS_HOST"),
    'PORT': 6379,
    'PASSWORD': get_secret("REDIS_PASSWORD")
}


MIDDLEWARE.insert(0, 'config.utility.middleware.ErrorLoggingMiddleWare')

ELASTIC_APM['ENVIRONMENT'] = 'production'
