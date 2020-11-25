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
    search_fields = ['email', 'first_name', 'last_name', 'passport_no']

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.UserSerializer
        elif self.action == 'retrieve':
            return serializers.UserDetailsSerializer

        return serializers.UserSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
 
class GroupFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter('id')

class GroupView(ModelViewSet):
    serializer_class = serializers.GroupSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = UserModel.objects.all().order_by('id')
 
    filter_class = GroupFilter
    search_fields = ['name']
