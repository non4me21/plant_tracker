from .base import *
import os
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

CORS_ORIGIN_ALLOW_ALL = DEBUG

ALLOWED_HOSTS = [
  'test'
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = { 
     
}

DATABASES["default"] = dj_database_url.parse(os.environ.get('DB_URL'))
