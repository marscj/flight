from django.db import models

# Create your models here.
class Apply(models.Model):

    remark = models.CharField(blank=True, null=True, max_length=256)
    
    author = models.ForeignKey(User, related_name='apply', on_delete=models.SET_NULL, blank=True, null=True)

class Reservation(models.Model):
    remark = models.CharField(blank=True, null=True, max_length=256)

    author = models.ForeignKey(User, related_name='reservation', on_delete=models.SET_NULL, blank=True, null=True)

class Ticket(models.Model):
    remark = models.CharField(blank=True, null=True, max_length=256)

    author = models.ForeignKey(User, related_name='ticket', on_delete=models.SET_NULL, blank=True, null=True)

class UpLoad(models.Model):
    author = models.ForeignKey(User, related_name='upload', on_delete=models.SET_NULL, blank=True, null=True)
