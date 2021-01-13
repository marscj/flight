from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, mixins
import django_filters

from middleware import viewset, permissions
from . import serializers
from . import models

class BookingFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter('id')
    date = django_filters.DateFromToRangeFilter('date')

class BookingView(viewset.ExtraModelViewSet):
    serializer_class = serializers.BookingSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = models.Booking.objects.all().order_by('-id')
 
    filter_class = BookingFilter
    search_fields = ['title', 'author__email', 'author__first_name', 'author__last_name']
      
    def get_queryset(self):
        if self.request.user.has_perm('ticket.view_booking'):
            return models.Booking.objects.all().order_by('-id')
        else :
            return super().get_queryset().filter(itineraries__user_id=self.request.user.id).distinct()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.messages.filter(user_id=self.request.user).update(read=True)
        return super().retrieve(request, *args, **kwargs)

class BookingHistoryFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter('id')
    history_id = django_filters.NumberFilter('history_id')
    date = django_filters.DateFromToRangeFilter('history_date')

class BookingHistoryView(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.BookingHistorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Booking.history.all().order_by('-id')
 
    filter_class = BookingHistoryFilter
    search_fields = ['title', 'history_user__email', 'history_user__first_name', 'history_user__last_name']

class ItineraryFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter('id')
    booking_id = django_filters.NumberFilter('booking__id')
    ticket_id = django_filters.NumberFilter('ticket__id')
    date = django_filters.DateFromToRangeFilter('date')

class ItineraryView(viewset.ExtraModelViewSet):
    serializer_class = serializers.ItinerarySerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = models.Itinerary.objects.all().order_by('-id')
 
    filter_class = ItineraryFilter
    search_fields = ['serial_no', 'email', 'name', 'passport_no']

    def get_queryset(self):
        if self.request.user.has_perm('ticket.view_itinerary'):
            return models.Itinerary.objects.all().order_by('-id')
        else :
            return super().get_queryset().filter(user_id=self.request.user.id).distinct()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.messages.filter(user=self.request.user).update(read=True)
        return super().retrieve(request, *args, **kwargs)


class ItineraryHistoryFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter('id')
    history_id = django_filters.NumberFilter('history_id')
    date = django_filters.DateFromToRangeFilter('history_date')
    booking_id = django_filters.NumberFilter('booking__id')
    ticket_id = django_filters.NumberFilter('ticket__id')

class ItineraryHistoryView(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.ItineraryHistorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Itinerary.history.all().order_by('-id')
 
    filter_class = ItineraryHistoryFilter
    search_fields = ['serial_no', 'email', 'name', 'passport_no']

class TicketFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter('id')
    date = django_filters.DateFromToRangeFilter('date')

class TicketView(viewset.ExtraModelViewSet):
    serializer_class = serializers.TicketSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = models.Ticket.objects.all().order_by('-id')
 
    filter_class = TicketFilter
    search_fields = ['serial_no', 'author__email', 'author__first_name', 'author__last_name']

    def get_queryset(self):
        if self.request.user.has_perm('ticket.view_ticket'):
            return models.Ticket.objects.all().order_by('-id')
        else :
            return super().get_queryset().filter(itineraries__user_id=self.request.user.id).distinct()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.messages.filter(user=self.request.user).update(read=True)
        return super().retrieve(request, *args, **kwargs)

class TicketHistoryFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter('id')
    history_id = django_filters.NumberFilter('history_id')
    date = django_filters.DateFromToRangeFilter('history_date')

class TicketHistoryView(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.TicketHistorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Ticket.history.all().order_by('-id')
 
    filter_class = TicketHistoryFilter
    search_fields = ['serial_no', 'history_user__email', 'history_user__first_name', 'history_user__last_name']

class UpLoadFilter(django_filters.FilterSet):
    object_id = django_filters.NumberFilter('object_id')
    type = django_filters.CharFilter('content_type__model')

class UpLoadView(viewset.ExtraModelViewSet):
    serializer_class = serializers.UpLoadSerializer
    permission_classes = [IsAuthenticated]
    queryset = models.UpLoad.objects.all().order_by('-id')
 
    filter_class = UpLoadFilter
    search_fields = ['']

class MessageFilter(django_filters.FilterSet):
    date = django_filters.DateFilter('date')
    week = django_filters.DateFromToRangeFilter('date')

class MessageView(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.MessageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Message.objects.all().order_by('-id')

    filter_class = MessageFilter

    def get_queryset(self):
        return models.Message.objects.filter(user=self.request.user).order_by('-id')