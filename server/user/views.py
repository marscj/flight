from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.conf import settings

from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from rest_framework import throttling
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
import django_filters

from . import serializers

UserModel = get_user_model()

class CustomLoginView(LoginView):
    throttle_classes = [throttling.AnonRateThrottle]

    def get_response(self):
        serializer_class = self.get_response_serializer()
 
        if getattr(settings, 'REST_USE_JWT', False):
            data = {
                'user': self.user,
                'token': self.token
            }
            serializer = serializer_class(instance=data,
                                          context={'request': self.request})
        else:
            serializer = serializer_class(instance=self.token,
                                          context={'request': self.request})

        response = Response(serializer.data, status=status.HTTP_200_OK)
        if getattr(settings, 'REST_USE_JWT', False) and self.serializer.data.get('remember', False):
            from rest_framework_jwt.settings import api_settings as jwt_settings
            if jwt_settings.JWT_AUTH_COOKIE:
                from datetime import datetime
                expiration = (datetime.utcnow() + jwt_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(jwt_settings.JWT_AUTH_COOKIE,
                                    self.token,
                                    expires=expiration,
                                    httponly=False)
        return response

class CustomRegisterView(RegisterView):
    queryset = UserModel.objects.all()

class UserFilter(django_filters.FilterSet):
    role = django_filters.NumberFilter('role')

class UserView(ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = UserModel.objects.filter(is_delete=False)
 
    filter_class = UserFilter
    search_fields = ['email', 'first_name', 'last_name', 'passport_no']
 
