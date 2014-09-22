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