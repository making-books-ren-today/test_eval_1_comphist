"""
Django settings for the dh@mit computational history project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

from .settings_base import *

# TODO(ra): replace this a fileread or env variable
SECRET_KEY = '9^vt7gzj#x_234%96*+-(a%j#h3($&s@(lrt-e)mhb=w#*56vz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['comphist-test.digitalhumanitiesmit.org']


# TODO(ra): production loggers to file / Sentry

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

