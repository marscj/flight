from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework import viewsets
import django_filters

from . import serializers
from . import models

class ApplyFilter(django_filters.FilterSet):
    role = django_filters.NumberFilter('role')

class ApplyView(viewsets.ModelViewSet):
    serializer_class = serializers.ApplySerializer
    permission_classes = [DjangoModelPermissions]
    queryset = models.Apply.objects.filter(is_delete=False)
 
    filter_class = ApplyFilter
    search_fields = ['']
 
