from django.db import models

# Create your models here.
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
    create_at = models.DateTimeField(auto_now_add=True)
    change_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, related_name='uploads', on_delete=models.SET_NULL, blank=True, null=True)
