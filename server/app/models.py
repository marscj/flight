from django.db import models

# Create your models here.
class App(models.Model):
    name = models.CharField(blank=True, null=True, max_length=64)

    version = models.CharField(blank=True, null=True, max_length=64)

    code = models.CharField(blank=Ture, null=True, max_length==64)

    