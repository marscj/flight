"""
Django settings for server project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path
import datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v+3qy6@buz#!50p16@m$c1)87daf7&%nom!*vzj0b#=cip&qk_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'server.urls'

AUTH_USER_MODEL = 'user.User'

WSGI_APPLICATION = 'server.wsgi.application'

SITE_ID = 1

# Application definition
INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'cacheops',
    'corsheaders',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'django_filters',

    'versatileimagefield',
    'simple_history',
    
    'authorization',
    'user',
    'ticket',
    'app',

    # 'django_celery_results'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

REST_FRAMEWORK = {
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M",
    'ORDERING_PARAM': 'sorter',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    # 自定义返回结果
    'DEFAULT_RENDERER_CLASSES': [
        'middleware.response.CustomJSONRenderer',
    ],
    'DEFAULT_THROTTLE_RATES': {   
        'anon': '3/m',
        'user': '100/m'
    },
    'DEFAULT_PAGINATION_CLASS': 'middleware.pagination.CustomPagination',
}

TEMPLATES = [
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 跨域
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = ('*',)
CORS_ALLOW_METHODS = ('*',)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dubai'

USE_I18N = True

USE_L10N = False

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'media')

# AllAuth
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'none'  # "mandatory", "optional", or "none"
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'SAADIYAT WAY'
ACCOUNT_MAX_EMAIL_ADDRESSES = 1
REST_USE_JWT = True
OLD_PASSWORD_FIELD_ENABLED = False

JWT_AUTH = { 
    'JWT_AUTH_HEADER_PREFIX': 'ACCESS_TOKEN',
    'JWT_AUTH_COOKIE' : 'Access-Token',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300)
}

REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'user.serializers.LoginSerializer',
    'USER_DETAILS_SERIALIZER': 'user.serializers.UserSerializer',
}

# REST_AUTH_REGISTER_SERIALIZERS = {
    
# }

REST_AUTH_REGISTER_PERMISSION_CLASSES = [
    'rest_framework.permissions.DjangoModelPermissions'
]

# 图片处理
VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    'image_size': [
        ('large', 'url'),
        ('medium', 'crop__400x400'),
        ('thumbnail', 'thumbnail__100x100')
    ]
}

CACHEOPS_DEFAULTS = {
    'timeout': 60 * 60
}

CACHEOPS = {
    '*.*': {},
}

#celery
BROKER_URL = "redis://redis:6379/0"
# CELERY_RESULT_BACKEND = "redis://redis:6379/0"
# CELERY_RESULT_BACKEND = 'django-db'

TIME_ZONE = 'Asia/Dubai'
CELERY_ENABLE_UTC = False
CELERYD_CONCURRENCY = 10
CELERYD_MAX_TASKS_PER_CHILD = 5
CELERY_SEND_EVENTS = True