from .settings import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

REST_FRAMEWORK = {
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M",
    'ORDERING_PARAM': 'sorter',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ),
    
    'DEFAULT_THROTTLE_RATES': {   
        'anon': '100/m',
        'user': '100/m'
    },
}