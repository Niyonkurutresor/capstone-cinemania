"""
Django settings for Cinemania project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
from distutils.debug import DEBUG

import os
import cloudinary_storage
import sys
import django_heroku


from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5*^0srl7r9n7jc6uhl8p#0%t17lp13+4*#+cr^_asw(-j&r!#g'

# SECURITY WARNING: don't run with debug turned on in production!
if (len(sys.argv) >= 2 and sys.argv[1] =='runserver'):
    DEBUG=True
else:
    DEBUG=False

ALLOWED_HOSTS = ['capstone-cinemania.herokuapp.com','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'members.apps.MembersConfig',
    'movies.apps.MoviesConfig',
    'django_filters',
    
   
 
  
]




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   
    
]

ROOT_URLCONF = 'Cinemania.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
               
            ],
        },
    },
]

WSGI_APPLICATION = 'Cinemania.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbaac5gsq4rl3i',
        'USER': 'ygtbahrvwskalv',
        'PASSWORD': '327569f2d7181c0de4cf3f72ff33de5bfa421d7aa66bb5d0c590b0536b2d7ce1',
        'HOST': 'ec2-54-85-56-210.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
import dj_database_url
db_from_env=dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'members.Members'


LOGIN_REDIRECT_URL = 'movies:favoritemovies'
LOGOUT_REDIRECT_URL = 'index'

STATIC_ROOT=os.path.join(BASE_DIR, "staticfiles/")
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static/"),
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # Base url to serve media files
# MEDIA_URL = '/media/'

# # Path where media is stored
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/image/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'image')
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'



django_heroku.settings(locals())

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dk87wja2c',
    'API_KEY': '391393736562449',
    'API_SECRET': 'H3q4qbwI-m_az5JnJ0gTzVmA-gM'
}
