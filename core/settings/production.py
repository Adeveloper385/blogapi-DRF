from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd87oevgkv580jo',
        'USER': 'ijdtmeykguptuk',
        'PASSWORD': 'dbb51bb374ca0735bba9b0392338d1c8506f26e1915345874d7c2a6507a91281',
        'HOST': 'ec2-52-23-87-65.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATIC_URL = '/static/'
