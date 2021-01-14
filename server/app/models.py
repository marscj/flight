from django.db import models
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver

class App(models.Model):
    
    class Type(models.TextChoices):
        IOS = 'Ios'
        ANDROID = 'Android'

    type = models.CharField(choices=Type.choices, default=Type.ANDROID, max_length=16)

    name = models.CharField(blank=True, null=True, max_length=64, unique=True)

    version = models.CharField(blank=True, null=True, max_length=64, unique=True)

    code = models.CharField(blank=True, null=True, max_length=16, unique=True)

    file = models.FileField(upload_to='uploads/app/', blank=True, null=True)

    redirect = models.URLField(blank=True, null=True)

    enable_redirect = models.BooleanField(default=False)

@receiver(pre_delete, sender=App)
def app_pre_delete(sender, instance, **kwargs):
    
    if instance.file is not None: 
        instance.file.delete()