from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.conf import settings

from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from rest_framework import throttling
from rest_auth.views import LoginView as AuthLoginView
from rest_auth.registration.views import RegisterView as AuthRegisterView
import django_filters 

from . import serializers

UserModel = get_user_model()

class LoginView(AuthLoginView):
    throttle_classes = [throttling.AnonRateThrottle]    

class RegisterView(AuthRegisterView):
    throttle_classes = [throttling.AnonRateThrottle]

class UserFilter(django_filters.FilterSet):
    role = django_filters.NumberFilter('role')

class UserView(ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = UserModel.objects.filter(is_delete=False)
 
    filter_class = UserFilter
    search_fields = ['email', 'first_name', 'last_name', 'passport_no']
 
