from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from user.models import User

class Apply(models.Model):
    remark = models.CharField(blank=True, null=True, max_length=256)
    create_at = models.DateTimeField(auto_now_add=True)
    change_at = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, related_name='applys', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'apply'

class Booking(models.Model):
    remark = models.CharField(blank=True, null=True, max_length=256)
    create_at = models.DateTimeField(auto_now_add=True)
    change_at = models.DateTimeField(auto_now=True)

    apply = models.ForeignKey(Apply, related_name='bookings', on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(User, related_name='bookings', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'booking'

class Ticket(models.Model):
    is_confirm = models.BooleanField(blank=True, null=True)
    is_cancel = models.BooleanField(blank=True, null=True)
    is_booking = models.BooleanField(blank=True, null=True)
    is_ticketing = models.BooleanField(blank=True, null=True)
    is_lock = models.BooleanField(default=False)

    remark = models.CharField(blank=True, null=True, max_length=256)
    create_at = models.DateTimeField(auto_now_add=True)
    change_at = models.DateTimeField(auto_now=True)

    booking = models.ForeignKey(Booking, related_name='tickets', on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(User, related_name='tickets', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'ticket'

class Comment(models.Model):
    comment = models.CharField(blank=True, null=True, max_length=256)
    read = models.BooleanField(blank=True, null=True, default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    
    booking = models.ForeignKey(Booking, related_name='comments', on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='comments', blank=True, null=True)

    class Meta:
        db_table = 'comment'

class UpLoad(models.Model):
    remark = models.CharField(blank=True, null=True, max_length=128)
    file = models.FileField(upload_to='upload/', blank=True)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    create_at = models.DateTimeField(auto_now_add=True)
    change_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, related_name='uploads', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'upload'

@receiver(pre_delete, sender=UpLoad)
def upload_pre_delete(sender, instance, **kwargs):
    
    if instance.file is not None: 
        instance.file.delete()