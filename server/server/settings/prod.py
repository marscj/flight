from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True

CACHEOPS_REDIS = "redis://redis:6379/0"

BROKER_URL = "redis://redis:6379/0"
CELERY_RESULT_BACKEND = "redis://redis:6379/0"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#db
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'Z)<f[>sOXXcBJ>wi',
        'HOST': 'db',
        'PORT': 5432,
    }
}

JWT_AUTH = { 
    'JWT_AUTH_HEADER_PREFIX': 'ACCESS_TOKEN',
    'JWT_AUTH_COOKIE' : 'Access-Token',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=30)
}