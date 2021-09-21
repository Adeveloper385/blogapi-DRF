from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dec61ctb4p23n4',
        'USER': 'khbeyqjumrddsd',
        'PASSWORD': '712a305abf733eb857ce2f3b9415e256fa129e5b2ac2a33871cbbc01f6095617',
        'HOST': 'ec2-44-193-150-214.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATIC_URL = '/static/'
