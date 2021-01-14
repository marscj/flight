from django.db import models

class App(models.Model):
    
    class Type(models.TextChoices):
        IOS = 'Ios'
        ANDROID = 'Android'

    type = models.CharField(choices=Type.choices, default=Type.ANDROID, max_length=16)

    name = models.CharField(blank=True, null=True, max_length=64)

    version = models.CharField(blank=True, null=True, max_length=64)

    code = models.CharField(blank=True, null=True, max_length=16)

    file = models.FileField(upload_to='uploads/app/', blank=True, null=True)