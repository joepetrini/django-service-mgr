from base import *

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gotya',
        'USER': 'joepetrini',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


INSTALLED_APPS += (
    'debug_toolbar.apps.DebugToolbarConfig',
)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'joepetrini'
EMAIL_HOST_PASSWORD = '3TheLimit'
DEFAULT_FROM_EMAIL = 'joepetrini@gmail.com'
#DEFAULT_TO_EMAIL = 'to email'