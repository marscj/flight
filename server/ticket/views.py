from django.shortcuts import render
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
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
            return super().get_queryset().filter(Q(itineraries__user_id=self.request.user.id) | Q(author_id=self.request.user.id)).distinct()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.messages.filter(user_id=self.request.user).update(read=True)
        return super().retrieve(request, *args, **kwargs)
    
    def get_extra_data(self):
        queryset = models.Message.objects.filter(Q(user=self.request.user) & Q(read=False)).order_by('-id')
        return {
            'messages': serializers.MessageSerializer(queryset, many=True).data,
        }

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
    ticket_id = django_filters.NumberFilter('tickets__id')
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

class ItineraryHistoryFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter('id')
    history_id = django_filters.NumberFilter('history_id')
    date = django_filters.DateFromToRangeFilter('history_date')
    booking_id = django_filters.NumberFilter('booking__id')
    ticket_id = django_filters.NumberFilter('tickets__id')

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
            if self.action == 'list':
                return models.Ticket.objects.filter(parent__isnull=True).order_by('-id')
            else:
                return models.Ticket.objects.all().order_by('-id')
        else:
            if self.action == 'list':
                return models.Ticket.objects.filter(Q(itinerary__user_id=self.request.user.id) & Q(parent__isnull=True)).order_by('-id').distinct()
            else:
                return models.Ticket.objects.filter(itinerary__user_id=self.request.user.id).order_by('-id').distinct()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
             
        if instance.parent is not None:
            instance.parent.messages.filter(user=self.request.user).update(read=True)
            for obj in instance.parent.children.all():
                obj.messages.filter(user=self.request.user).update(read=True)
        else:
            instance.messages.filter(user=self.request.user).update(read=True)
            for obj in instance.children.all():
                obj.messages.filter(user=self.request.user).update(read=True)

        return super().retrieve(request, *args, **kwargs)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def confirm(self, request, pk=None):
        data = self.get_object()
        serializer = serializers.ConfirmTicketSerializer(data=request.data)
        status = None

        if serializer.is_valid():
            if serializer.data['confirm']:
                status = 3
            else:
                status = 4
                
            if data.type_status == 0:
                data.normal_status = status

            if data.type_status == 1:
                data.change_status = status

            if data.type_status == 2:
                data.cancel_status = status

            data.save()

            if not serializer.data['confirm']:
                models.Comment.objects.create(content=serializer.data['reason'], object_id=data.id, content_type=ContentType.objects.get(model='ticket'), user=request.user)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'data': serializers.TicketSerializer(instance=data).data})

    def get_extra_data(self):
        queryset = models.Message.objects.filter(Q(user=self.request.user) & Q(read=False)).order_by('-id')
        return {
            'messages': serializers.MessageSerializer(queryset, many=True).data,
        }

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
    content_type = django_filters.CharFilter('content_type__model')

class UpLoadView(viewset.ExtraModelViewSet):
    serializer_class = serializers.UpLoadSerializer
    permission_classes = [IsAuthenticated]
    queryset = models.UpLoad.objects.all().order_by('-id')
 
    filter_class = UpLoadFilter
    search_fields = ['']

class MessageFilter(django_filters.FilterSet):
    date = django_filters.DateFilter('date')
    week = django_filters.DateFromToRangeFilter('date')
    read = django_filters.BooleanFilter('read')

class MessageView(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.MessageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Message.objects.all().order_by('-id')

    filter_class = MessageFilter

    def get_queryset(self):
        return models.Message.objects.filter(user=self.request.user).order_by('-id')

class CommentFilter(django_filters.FilterSet):
    object_id = django_filters.NumberFilter('object_id')
    content_type = django_filters.CharFilter('content_type__model')

class CommentView(viewset.ExtraModelViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticated]
    queryset = models.Comment.objects.all().order_by('-id')
 
    filter_class = CommentFilter
    search_fields = ['']        