from django.db.models import Q
from django.dispatch import receiver
from django.db.models.signals import pre_delete, post_save

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
from plugs import push, message



@receiver(post_create_historical_record)
def post_create_historical_record_callback(sender, instance, history_instance, history_user, **kwargs):

    serializer = None

    if history_instance.history_type == '-':
        instance.messages.all().delete()
        instance.comments.all().delete()
            
        if type(instance).__name__ == 'Booking':
            instance.itineraries.all().delete()

        if type(instance).__name__ == 'Ticket':
            instance.children.all().delete()
        
        return 
    
    if type(instance).__name__ == 'Booking':
        serializer = BookingHistorySerializer(instance=history_instance).data
        serializer['model'] = type(instance).__name__
        
        #admin推送
        for user in User.objects.filter(Q(is_staff=True) & ~Q(id=history_instance.history_user.id)):
            Message.objects.create(json=serializer, content_object=instance, user=user)
            message.send_admin_message.delay('{user} {action} Booking for ID: {id}'.format(user=history_instance.history_user, action=ActionString.get(history_instance.history_type), id=history_instance.id), user.email)

        #客户推送
        #for itinerary in instance.itineraries.all():
            # Message.objects.create(json=serializer, content_object=instance, user=itinerary.user)
            #message.send_admin_message.delay('{user} {action} Booking for ID: {id}'.format(user=history_instance.history_user, action=ActionString.get(history_instance.history_type), id=history_instance.id), itinerary.user.email)

    if type(instance).__name__ == 'Ticket':
        serializer = TicketHistorySerializer(instance=history_instance).data
        serializer['model'] = type(instance).__name__
        
        #admin推送
        for user in User.objects.filter(Q(is_staff=True) & ~Q(id=history_instance.history_user.id)):
            Message.objects.create(json=serializer, content_object=instance, user=user)
            message.send_admin_message.delay('{user} {action} Ticket for ID: {id}'.format(user=history_instance.history_user, action=ActionString.get(history_instance.history_type), id=history_instance.id), user.email)
        
        #客户推送
        if instance.itinerary is not None and instance.itinerary.user is not None:
            Message.objects.create(json=serializer, content_object=instance, user=instance.itinerary.user)
            message.send_admin_message.delay('{user} {action} Ticket for ID: {id}'.format(user=history_instance.history_user, action=ActionString.get(history_instance.history_type), id=history_instance.id), instance.itinerary.user.email)

    if type(instance).__name__ == 'Itinerary':
        serializer = ItineraryHistorySerializer(instance=history_instance).data
        serializer['model'] = type(instance).__name__
        
        #admin推送
        for user in User.objects.filter(Q(is_staff=True) & ~Q(id=history_instance.history_user.id)):
            Message.objects.create(json=serializer, content_object=instance.booking, user=user)
            message.send_admin_message.delay('{user} {action} Itinerary for ID: {id}'.format(user=history_instance.history_user, action=ActionString.get(history_instance.history_type), id=history_instance.id), user.email)

        #客户推送
        #if instance.user is not None:
            # Message.objects.create(js on=serializer, content_object=instance, user=itinerary.user)
            #message.send_admin_message.delay('{user} {action} Itinerary for ID: {id}'.format(user=history_instance.history_user, action=ActionString.get(history_instance.history_type), id=history_instance.id), instance.user.email)
