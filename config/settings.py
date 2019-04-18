"""
Django settings for the dh@mit computational history project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from django_jinja.builtins import DEFAULT_EXTENSIONS
from utilities.jinja_utils import collect_jinja2_functions

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(CONFIG_DIR)
DATA_DIR = os.path.join(ROOT_DIR, 'data')
METADATA_CSV = os.path.join(DATA_DIR, 'metadata.csv')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9^vt7gzj#x_234%96*+-(a%j#h3($&s@(lrt-e)mhb=w#*56vz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # core django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party apps
    'django_jinja',  # we use Jinja2 templates, not pure django.
    'django_jinja.contrib._humanize',

    # our apps
    'apps.archives',
    'apps.simulations',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        'DIRS': [(os.path.join(ROOT_DIR, 'templates'))],
        'APP_DIRS': True,
        "OPTIONS": {
            'trim_blocks': True,
            'autoescape': True,
            'lstrip_blocks': True,
            'match_extension': '.jinja2',
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.static",
                "django.contrib.messages.context_processors.messages",
            ],
            "extensions": DEFAULT_EXTENSIONS + [
                'jdj_tags.extensions.DjangoStatic',  # this emulates the {% static %} tag
                'jdj_tags.extensions.DjangoUrl',  # this emulates the {% url %} tag
                'jdj_tags.extensions.DjangoCsrf',  # this emulates the {% csrf_token %} tag
            ],
        }
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

DEFAULT_JINJA2_TEMPLATE_EXTENSION = ".jinja2"
JINJA2_ENVIRONMENT_OPTIONS = {
    'trim_blocks': True,
    'autoescape': True,
    'lstrip_blocks': True
}
JINJA2_FILTERS = collect_jinja2_functions()  # gets functions and filters

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'sqlite3': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_DIR, 'db.sqlite3'),
    },

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'comphist-test-0.cdciclcuqo67.us-west-1.rds.amazonaws.com',
        'PORT': '5432',
        'NAME': 'comphist_test',
        'USER': 'comphist_readonly',
        'PASSWORD': 'readonly',
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/ 
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, 'assets')  # collectstatic puts everything here
STATICFILES_DIRS = [
    os.path.join(ROOT_DIR, 'static'), # put all static files here (or in app folders) in development
]



# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'WARNING',
        'handlers': ['console'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
        'db_queries': {
            'format': '\nDB Query - %(asctime)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'console_db': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'db_queries'
        },
    },
    'loggers': {
#        'django.db.backends': {
#            'level': 'DEBUG',
#            'handlers': ['console_db'],
#            'propagate': False,
#        },
    },
}

