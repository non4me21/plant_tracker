from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CORS_ORIGIN_ALLOW_ALL = DEBUG

ALLOWED_HOSTS = [
    'web',
    'localhost'
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {    
   "default": {        
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",
        "PORT": 5432,
    }
}
