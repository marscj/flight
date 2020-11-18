from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.conf import settings

from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
import django_filters 

from . import serializers

UserModel = get_user_model()

class UserFilter(django_filters.FilterSet):
    role = django_filters.NumberFilter('role')

class UserView(ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = UserModel.objects.filter(is_delete=False)
 
    filter_class = UserFilter
    search_fields = ['email', 'first_name', 'last_name', 'passport_no']
 
