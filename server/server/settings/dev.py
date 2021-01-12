from .settings import *

DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True

CACHEOPS_REDIS = "redis://localhost:6379/0"

BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = 'django-db'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

JWT_AUTH = { 
    'JWT_AUTH_HEADER_PREFIX': 'ACCESS_TOKEN',
    'JWT_AUTH_COOKIE' : 'Access-Token',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1)
}