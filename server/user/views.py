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
    id = django_filters.NumberFilter('id')

class UserView(ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = UserModel.objects.all().order_by('id')

    filter_class = UserFilter
    ordering = ['-id']
    search_fields = ['email', 'first_name', 'last_name', 'passport_no']
 
class GroupFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter('id')

class GroupView(ModelViewSet):
    serializer_class = serializers.GroupSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = UserModel.objects.all().order_by('id')
 
    filter_class = GroupFilter
    ordering = ['-id']
    search_fields = ['name']
