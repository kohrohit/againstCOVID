from .base import *

DEBUG = True

STATIC_URL = '/static/'

STATIC_ROOT = str(BASE_DIR / 'static')

# psql --host 127.0.0.1 --username ert_user -W --port 5433 ert
# psql -h 127.0.0.1 -p 5432 -U abhisheksingh -W postgres
# psql -h 127.0.0.1 -p 5432 -U root -W ert

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

REDIS_CONFIG = {
    'HOST': get_secret("REDIS_HOST"),
    'PORT': 6379,
    'PASSWORD': get_secret("REDIS_PASSWORD")
}

# Elastic-APM settings

ELASTIC_APM['ENVIRONMENT'] = 'local'
# uncomment this if apm logging needs to be enabled for local testing
ELASTIC_APM['DEBUG'] = True

# debug-toolbar settings

INTERNAL_IPS = ('127.0.0.1', 'localhost',)

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

INSTALLED_APPS.append('debug_toolbar')

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
