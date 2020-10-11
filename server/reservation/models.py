from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from versatileimagefield.fields import VersatileImageField, PPOIField
from user.models import User

class Apply(models.Model):
    remark = models.CharField(blank=True, null=True, max_length=256)
    create_at = models.DateTimeField(auto_now_add=True)
    change_at = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, related_name='applys', on_delete=models.SET_NULL, blank=True, null=True)

class Reservation(models.Model):
    remark = models.CharField(blank=True, null=True, max_length=256)
    create_at = models.DateTimeField(auto_now_add=True)
    change_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, related_name='reservations', on_delete=models.SET_NULL, blank=True, null=True)

class Ticket(models.Model):
    remark = models.CharField(blank=True, null=True, max_length=256)
    create_at = models.DateTimeField(auto_now_add=True)
    change_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, related_name='tickets', on_delete=models.SET_NULL, blank=True, null=True)

class UpLoad(models.Model):
    tag = models.CharField(max_length=128)
    file = models.FileField(upload_to='upload/', blank=True)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    create_at = models.DateTimeField(auto_now_add=True)
    change_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, related_name='uploads', on_delete=models.SET_NULL, blank=True, null=True)
