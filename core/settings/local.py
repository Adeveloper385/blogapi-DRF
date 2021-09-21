from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test',
        'USER': 'user1',
        'PASSWORD': 'j2osqcdm',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

STATIC_URL = '/static/'
