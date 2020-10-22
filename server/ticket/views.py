from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework import viewsets
import django_filters

from . import serializers
from . import models

class ApplyFilter(django_filters.FilterSet):
    pass

class ApplyView(viewsets.ModelViewSet):
    serializer_class = serializers.ApplySerializer
    permission_classes = [DjangoModelPermissions]
    queryset = models.Apply.objects.filter(is_delete=False)
 
    filter_class = ApplyFilter
    search_fields = ['']
 
class ItineraryFilter(django_filters.FilterSet):
    pass

class ItineraryView(viewsets.ModelViewSet):
    serializer_class = serializers.ItinerarySerializer
    permission_classes = [DjangoModelPermissions]
    queryset = models.Itinerary.objects.filter(is_delete=False)
 
    filter_class = ItineraryFilter
    search_fields = ['']

class TicketFilter(django_filters.FilterSet):
    pass

class TicketView(viewsets.ModelViewSet):
    serializer_class = serializers.TicketSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = models.Ticket.objects.filter(is_delete=False)
 
    filter_class = TicketFilter
    search_fields = ['']

class CommentFilter(django_filters.FilterSet):
    pass

class CommentView(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = models.Comment.objects.filter(is_delete=False)
 
    filter_class = CommentFilter
    search_fields = ['']

class UpLoadFilter(django_filters.FilterSet):
    pass

class UpLoadView(viewsets.ModelViewSet):
    serializer_class = serializers.UpLoadSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = models.UpLoad.objects.all()
 
    filter_class = UpLoadFilter
    search_fields = ['']