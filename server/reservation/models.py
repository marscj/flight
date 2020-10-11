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

class Reservation(models.Model):
    remark = models.CharField(blank=True, null=True, max_length=256)
    create_at = models.DateTimeField(auto_now_add=True)
    change_at = models.DateTimeField(auto_now=True)

    apply = models.ForeignKey(Apply, related_name='reservations', on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(User, related_name='reservations', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'reservation'

class Ticket(models.Model):
    remark = models.CharField(blank=True, null=True, max_length=256)
    create_at = models.DateTimeField(auto_now_add=True)
    change_at = models.DateTimeField(auto_now=True)

    reservation = models.ForeignKey(Reservation, related_name='tickets', on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(User, related_name='tickets', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'ticket'

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
    
    if instance.uploads is not None: 
        instance.uploads.delete()