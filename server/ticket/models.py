import uuid
from django.db import models
from django.db.models import Value
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver

from simple_history.models import HistoricalRecords
from simple_history.signals import (
    pre_create_historical_record,
    post_create_historical_record
)

from user.models import User
from push import push

class Message(models.Model):
    
    json = models.JSONField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    read = models.BooleanField(default=False, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(User, related_name='messages', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'message'

def file_path_name(instance, filename):
    file_path = 'uploads/{model}/{id}/{filename}'.format(model=instance.content_type.model, id=instance.object_id, filename=filename) 
    return file_path

class UpLoad(models.Model):

    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    remark = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to=file_path_name, blank=True)
    date = models.DateField(auto_now_add=True)  
    author = models.ForeignKey(User, related_name='uploads', on_delete=models.SET_NULL, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        db_table = 'upload'

class Booking(models.Model):
    title = models.CharField(blank=True, null=True, max_length=64)
    remark = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    
    uploads = GenericRelation(UpLoad, related_query_name='booking')
    messages = GenericRelation(Message, related_query_name='booking')
    author = models.ForeignKey(User, related_name='bookings', on_delete=models.SET_NULL, blank=True, null=True)
    history = HistoricalRecords(table_name='booking_history', custom_model_name='booking_history')

    class Meta:
        db_table = 'booking'

class Ticket(models.Model):
    serial_no = models.CharField(blank=True, null=True, max_length=32)
    air_line = models.CharField(blank=True, null=True, max_length=16)
    air_info = models.CharField(blank=True, null=True, max_length=1024)
    air_class = models.CharField(blank=True, null=True, max_length=64)
    fare = models.FloatField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    is_confirm = models.BooleanField(default=False, blank=True, null=True)
    is_cancel = models.BooleanField(default=False, blank=True, null=True)
    is_booking = models.BooleanField(default=True, blank=True, null=True)
    is_complete = models.BooleanField(default=False, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    
    messages = GenericRelation(Message, related_query_name='ticket')
    uploads = GenericRelation(UpLoad, related_query_name='ticket')
    author = models.ForeignKey(User, related_name='ticket_authors', on_delete=models.SET_NULL, blank=True, null=True)
    history = HistoricalRecords(table_name='ticket_history', custom_model_name='ticket_history')

    class Meta:
        db_table = 'ticket'

class Itinerary(models.Model):
    serial_no = models.CharField(blank=True, null=True, max_length=32)
    email = models.CharField(blank=True, null=True, max_length=64)
    name = models.CharField(blank=True, null=True, max_length=64)
    passport_no = models.CharField(blank=True, null=True, max_length=16)
    entry = models.CharField(blank=True, null=True, max_length=256)
    exit = models.CharField(blank=True, null=True, max_length=256)
    ticket1 = models.CharField(blank=True, null=True, max_length=256)
    ticket2 = models.CharField(blank=True, null=True, max_length=256)
    hotel = models.CharField(blank=True, null=True, max_length=256)
    is_lock = models.BooleanField(default=False, null=True)
    remark = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    
    messages = GenericRelation(Message, related_query_name='itinerary')
    uploads = GenericRelation(UpLoad, related_query_name='itinerary')
    user = models.ForeignKey(User, related_name='itinerary_users', on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(User, related_name='itinerary_authors', on_delete=models.SET_NULL, blank=True, null=True)
    booking = models.ForeignKey(Booking, related_name='itineraries', on_delete=models.SET_NULL, blank=True, null=True)
    ticket = models.ForeignKey(Ticket, related_name='itineraries', on_delete=models.SET_NULL, blank=True, null=True)

    history = HistoricalRecords(table_name='itinerary_history', custom_model_name='itinerary_history')

    class Meta:
        db_table = 'itinerary'
        permissions = (
            ('lock_itinerary', 'Can lock itinerary'),
        )

@receiver(pre_delete, sender=UpLoad)
def upload_pre_delete(sender, instance, **kwargs):
    
    if instance.file is not None: 
        instance.file.delete()

# @receiver(post_save, sender=Booking)
# def booking_post_save(sender, instance, created, **kwargs):

#     body = None
#     if created:
#         body = 'customer created a booking'
#     else:
#         body = 'customer modified the booking information'

#     push.send_message('You have a new message', body, tag=['haha'])

@receiver(post_create_historical_record)
def post_create_historical_record_callback(sender, instance, history_instance, history_user, **kwargs):
    
    serializer = None
    if type(instance).__name__ == 'Booking':
        serializer = BookingHistorySerializer(instance=history_instance).data
        serializer['model'] = type(instance).__name__
        models.Message.objects.create(json=serializer)

    if type(instance).__name__ == 'Ticket':
        serializer = TicketHistorySerializer(instance=history_instance).data
        serializer['model'] = type(instance).__name__
        models.Message.objects.create(json=serializer)

    if type(instance).__name__ == 'Itinerary':
        serializer = ItineraryHistorySerializer(instance=history_instance).data
        serializer['model'] = type(instance).__name__
        
        role in Group.objects.filter(permissions__name='view_itinerary'):
            user in role.user.all():
                models.Message.objects.create(json=serializer, content_type=ContentType.objects.get(model=type(instance).__name__), object_id= instance.id, user=user)