from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, mixins
import django_filters

from middleware import viewset, permissions
from . import serializers
from . import models

class BookingFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter('id')


class BookingView(viewset.ExtraModelViewSet):
    serializer_class = serializers.BookingSerializer
    permission_classes = [IsAuthenticated, permissions.ModelPermissions]
    queryset = models.Booking.objects.all().order_by('-id')
 
    filter_class = BookingFilter
    search_fields = ['']
      
    def get_queryset(self):
        if self.request.user.has_perm('ticket.view_booking'):
            return models.Booking.objects.all().order_by('-id')
        else :
            return super().get_queryset().filter(itineraries__user_id=self.request.user.id).distinct()

class BookingHistoryView(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.BookingHistorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Booking.history.all().order_by('-id')
 
    filter_class = BookingFilter
    search_fields = ['title', 'author__email', 'author__first_name', 'author__last_name']

class ItineraryFilter(django_filters.FilterSet):
    booking_id = django_filters.NumberFilter('booking_id')

class ItineraryView(viewsets.ModelViewSet):
    serializer_class = serializers.ItinerarySerializer
    permission_classes = [DjangoModelPermissions, IsAuthenticated]
    queryset = models.Itinerary.objects.all().order_by('id')
 
    filter_class = ItineraryFilter
    search_fields = ['']

class TicketFilter(django_filters.FilterSet):
    pass

class TicketView(viewsets.ModelViewSet):
    serializer_class = serializers.TicketSerializer
    permission_classes = [DjangoModelPermissions, IsAuthenticated]
    queryset = models.Ticket.objects.all().order_by('id')
 
    filter_class = TicketFilter
    search_fields = ['']

class CommentFilter(django_filters.FilterSet):
    pass

class CommentView(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = [DjangoModelPermissions, IsAuthenticated]
    queryset = models.Comment.objects.all().order_by('id')
 
    filter_class = CommentFilter
    search_fields = ['']

class UpLoadFilter(django_filters.FilterSet):
    pass

class UpLoadView(viewsets.ModelViewSet):
    serializer_class = serializers.UpLoadSerializer
    permission_classes = [DjangoModelPermissions, IsAuthenticated]
    queryset = models.UpLoad.objects.all().order_by('id')
 
    filter_class = UpLoadFilter
    search_fields = ['']