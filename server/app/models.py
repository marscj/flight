from django.db import models

def file_path_name(instance, filename):
    file_path = 'uploads/app/'.format(model=instance.content_type.model, id=instance.object_id, filename=filename) 
    return file_path

class App(models.Model):
    
    class Type(models.TextChoices):
        IOS = 'Ios'
        ANDROID = 'Android'

    type = models.CharField(choices=Type.choices, default=Type.ANDROID, max_length=16)

    name = models.CharField(blank=True, null=True, max_length=64)

    version = models.CharField(blank=True, null=True, max_length=64)

    code = models.CharField(blank=Ture, null=True, max_length=16)

    file = models.FileField(upload_to=file_path_name, blank=True)