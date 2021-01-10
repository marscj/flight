from django.db.models import Q
from django.dispatch import receiver
from simple_history.signals import (
    pre_create_historical_record,
    post_create_historical_record
)

from user.models import User

ActionString = {
  '+': 'Added',
  '~': 'Changed',
  '-': 'Deleted'
}

from .serializers import BookingHistorySerializer, TicketHistorySerializer, ItineraryHistorySerializer
from .models import Message
from push import push

@receiver(post_create_historical_record)
def post_create_historical_record_callback(sender, instance, history_instance, history_user, **kwargs):
    
    serializer = None
    
    if type(instance).__name__ == 'Booking':
        serializer = BookingHistorySerializer(instance=history_instance).data
        serializer['model'] = type(instance).__name__
        
        for user in User.objects.filter(Q(is_staff=True) & ~Q(id=history_instance.history_user.id)):
            Message.objects.create(json=serializer, content_object=instance, user=user)
        
        if(history_instance.history_user.is_staff):
            push.send_message('{user} {action} Booking for ID: {id}'.format(user=history_instance.history_user, action=ActionString.get(history_instance.history_type), id=history_instance.id), tag=['customer'])
        else:
            push.send_message('{user} {action} Booking for ID: {id}'.format(user=history_instance.history_user, action=ActionString.get(history_instance.history_type), id=history_instance.id), tag=['staff'])
        
    if type(instance).__name__ == 'Ticket':
        serializer = TicketHistorySerializer(instance=history_instance).data
        serializer['model'] = type(instance).__name__
        
        for user in User.objects.filter(Q(is_staff=True) & ~Q(id=history_instance.history_user.id)):
            Message.objects.create(json=serializer, content_object=instance, user=user)
        
        if(history_instance.history_user.is_staff):
            push.send_message('{user} {action} Ticket for ID: {id}'.format(user=history_instance.history_user, action=ActionString.get(history_instance.history_type), id=history_instance.id), tag=['customer'])
        else:
            push.send_message('{user} {action} Ticket for ID: {id}'.format(user=history_instance.history_user, action=ActionString.get(history_instance.history_type), id=history_instance.id), tag=['staff'])

    if type(instance).__name__ == 'Itinerary':
        serializer = ItineraryHistorySerializer(instance=history_instance).data
        serializer['model'] = type(instance).__name__
        
        for user in User.objects.filter(Q(is_staff=True) & ~Q(id=history_instance.history_user.id)):
            Message.objects.create(json=serializer, content_object=instance, user=user)

        if(history_instance.history_user.is_staff):
            push.send_message('{user} {action} Itinerary for ID: {id}'.format(user=history_instance.history_user, action=ActionString.get(history_instance.history_type), id=history_instance.id), tag=['customer'])
        else:
            push.send_message('{user} {action} Itinerary for ID: {id}'.format(user=history_instance.history_user, action=ActionString.get(history_instance.history_type), id=history_instance.id), tag=['staff'])