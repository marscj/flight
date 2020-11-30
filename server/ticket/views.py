from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework import viewsets
import django_filters

from . import serializers
from . import models
from . import permissions

class BookingFilter(django_filters.FilterSet):
    pass

class BookingView(viewsets.ModelViewSet):
    serializer_class = serializers.BookingSerializer
    permission_classes = [permissions.ModelPermissions, permissions.IsOwnerOrReadOnly]
    queryset = models.Booking.objects.all().order_by('id')
 
    filter_class = BookingFilter
    search_fields = ['']

    def get_queryset(self):
        if self.request.user.has_perm('ticket.view_apply'):
            return models.Apply.objects.all()
        else :
            return super().get_queryset().filter(itinerarys__user_id=self.request.user.id).distinct()
 
class ItineraryFilter(django_filters.FilterSet):
    pass

class ItineraryView(viewsets.ModelViewSet):
    serializer_class = serializers.ItinerarySerializer
    permission_classes = [DjangoModelPermissions, permissions.IsOwnerOrReadOnly]
    queryset = models.Itinerary.objects.all().order_by('id')
 
    filter_class = ItineraryFilter
    search_fields = ['']

class TicketFilter(django_filters.FilterSet):
    pass

class TicketView(viewsets.ModelViewSet):
    serializer_class = serializers.TicketSerializer
    permission_classes = [DjangoModelPermissions, permissions.IsOwnerOrReadOnly]
    queryset = models.Ticket.objects.all().order_by('id')
 
    filter_class = TicketFilter
    search_fields = ['']

class CommentFilter(django_filters.FilterSet):
    pass

class CommentView(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = [DjangoModelPermissions, permissions.IsOwnerOrReadOnly]
    queryset = models.Comment.objects.all().order_by('id')
 
    filter_class = CommentFilter
    search_fields = ['']

class UpLoadFilter(django_filters.FilterSet):
    pass

class UpLoadView(viewsets.ModelViewSet):
    serializer_class = serializers.UpLoadSerializer
    permission_classes = [DjangoModelPermissions, permissions.IsOwnerOrReadOnly]
    queryset = models.UpLoad.objects.all().order_by('id')
 
    filter_class = UpLoadFilter
    search_fields = ['']