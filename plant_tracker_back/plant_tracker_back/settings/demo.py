from .base import *
import os
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CORS_ORIGIN_ALLOW_ALL = DEBUG

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', 'planttracker-production.up.railway.app').split(',')

import os
print(f"ALLOWED_HOSTS: {ALLOWED_HOSTS}")

CSRF_TRUSTED_ORIGINS = ['https://planttracker-production.up.railway.app', 'http://planttracker-production.up.railway.app']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = { 
     
}

DATABASES["default"] = dj_database_url.parse(os.environ.get('DB_URL'))
