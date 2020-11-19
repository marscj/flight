from .settings import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

JWT_AUTH = { 
    'JWT_AUTH_HEADER_PREFIX': 'ACCESS_TOKEN',
    'JWT_AUTH_COOKIE' : 'Access-Token',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1)
}