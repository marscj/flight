from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from simple_history.models import HistoricalRecords

from user.models import User

class Booking(models.Model):
    title = models.CharField(blank=True, null=True, max_length=64)
    remark = models.CharField(blank=True, null=True, max_length=1024)

    author = models.ForeignKey(User, related_name='bookings', on_delete=models.SET_NULL, blank=True, null=True)

    history = HistoricalRecords(table_name='booking_history', custom_model_name='booking_history')

    class Meta:
        db_table = 'booking'

class Ticket(models.Model):
    serial_no = models.CharField(blank=True, null=True, max_length=32)
    name = models.CharField(blank=True, null=True, max_length=64)
    airline = models.CharField(blank=True, null=True, max_length=16)
    air_information = models.CharField(blank=True, null=True, max_length=1024)
    air_class = models.CharField(blank=True, null=True, max_length=64)
    fare = models.FloatField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    remark = models.CharField(blank=True, null=True, max_length=256)
    is_confirm = models.BooleanField(default=False)
    is_cancel = models.BooleanField(default=False)
    is_booking = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)

    user = models.ForeignKey(User, related_name='ticket_users', on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(User, related_name='ticket_authors', on_delete=models.SET_NULL, blank=True, null=True)

    history = HistoricalRecords(table_name='ticket_history', custom_model_name='ticket_history')

    class Meta:
        db_table = 'ticket'

class Itinerary(models.Model):
    serial_no = models.CharField(unique=True, blank=True, null=True, max_length=32)
    name = models.CharField(blank=True, null=True, max_length=64)
    email = models.CharField(blank=True, null=True, max_length=64)
    passport_no = models.CharField(blank=True, null=True, max_length=16)
    entry = models.CharField(blank=True, null=True, max_length=256)
    exit = models.CharField(blank=True, null=True, max_length=256)
    ticket1 = models.CharField(blank=True, null=True, max_length=256)
    ticket2 = models.CharField(blank=True, null=True, max_length=256)
    hotel = models.CharField(blank=True, null=True, max_length=256)
    is_lock = models.BooleanField(default=False, null=True)
    remark = models.CharField(blank=True, null=True, max_length=256)

    user = models.ForeignKey(User, related_name='itinerary_users', on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(User, related_name='itinerary_authors', on_delete=models.SET_NULL, blank=True, null=True)
    booking = models.ForeignKey(Booking, related_name='itineraries', on_delete=models.SET_NULL, blank=True, null=True)
    ticket = models.ForeignKey(Ticket, related_name='tickets', on_delete=models.SET_NULL, blank=True, null=True)

    history = HistoricalRecords(table_name='itinerary_history', custom_model_name='itinerary_history')

    class Meta:
        db_table = 'itinerary'
        permissions = (
            ('lock_itinerary', 'Can lock itinerary'),
        )

class Comment(models.Model):
    comment = models.CharField(blank=True, null=True, max_length=256)

    itinerary = models.ForeignKey(Itinerary, related_name='comments', on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='comments', blank=True, null=True)

    class Meta:
        db_table = 'comment'

class UpLoad(models.Model):
    remark = models.CharField(blank=True, null=True, max_length=128)
    file = models.FileField(upload_to='upload/', blank=True)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    author = models.ForeignKey(User, related_name='uploads', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'upload'

@receiver(pre_delete, sender=UpLoad)
def upload_pre_delete(sender, instance, **kwargs):
    pass