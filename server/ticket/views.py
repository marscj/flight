from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, mixins
import django_filters

from middleware import viewset, permissions
from . import serializers
from . import models

class BookingFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter('-id')

class BookingView(viewset.ExtraModelViewSet):
    serializer_class = serializers.BookingSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
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
    booking_id = django_filters.NumberFilter('booking__id')
    ticket_id = django_filters.NumberFilter('ticket__id')


class ItineraryView(viewset.ExtraModelViewSet):
    serializer_class = serializers.ItinerarySerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = models.Itinerary.objects.all().order_by('-id')
 
    filter_class = ItineraryFilter
    search_fields = ['']

class ItineraryHistoryView(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.ItineraryHistorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Itinerary.history.all().order_by('-id')
 
    filter_class = ItineraryFilter
    search_fields = ['']

class TicketFilter(django_filters.FilterSet):
    pass

class TicketView(viewset.ExtraModelViewSet):
    serializer_class = serializers.TicketSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = models.Ticket.objects.all().order_by('-id')
 
    filter_class = TicketFilter
    search_fields = ['']

class TicketHistoryView(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.TicketHistorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Ticket.history.all().order_by('-id')
 
    filter_class = TicketFilter
    search_fields = ['']

class CommentFilter(django_filters.FilterSet):
    pass

class CommentView(viewset.ExtraModelViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = models.Comment.objects.all().order_by('-id')
 
    filter_class = CommentFilter
    search_fields = ['']

class UpLoadFilter(django_filters.FilterSet):
    pass

class UpLoadView(viewset.ExtraModelViewSet):
    serializer_class = serializers.UpLoadSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = models.UpLoad.objects.all().order_by('-id')
 
    filter_class = UpLoadFilter
    search_fields = ['']