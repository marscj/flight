from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from versatileimagefield.fields import VersatileImageField, PPOIField
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):

    class Role(models.IntegerChoices):
        Staff = 0
        Admin = 1
        SupserAdmin = 2

    name = models.CharField(blank=True, null=True, max_length=16)
    phone = PhoneNumberField(unique=True, blank=True, null=True)
    avatar = VersatileImageField(upload_to='user/avatar/', ppoi_field='image_ppoi', null=True, blank=True)
    image_ppoi = PPOIField()

    class Meta:
        db_table = 'user'

class Passport(models.Model):
    model = models.CharField(max_length=8)
    code = models.CharField(max_length=8)
    number = models.CharField(unique=True, max_length=16)
    name = models.CharField(max_length=32)
    gender = models.IntegerField()
    nationality = models.CharField(max_length=64)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=64)
    issue_date = models.DateField()
    issue_place = models.CharField(max_length=64)
    expiry_date = models.DateField()
    authority = models.CharField(max_length=64)

    front_photo = VersatileImageField(upload_to='user/passport/', ppoi_field='image_ppoi', null=True, blank=True)
    back_photo = VersatileImageField(upload_to='user/passport/', ppoi_field='image_ppoi', null=True, blank=True)
    image_ppoi = PPOIField()
    user = models.ForeignKey(User, related_name='passport', on_delete=models.CASCADE)


class Id(models.Model):
    name = models.CharField(max_length=32)
    gender = models.IntegerField()
    clan = models.CharField(max_length=8)
    birth_date = models.DateField()
    address = models.CharField(max_length=128)
    expiry_date = models.DateField()
    authority = models.CharField(max_length=64)
    number = models.CharField(unique=True, max_length=16)

    front_photo = VersatileImageField(upload_to='user/id/', ppoi_field='image_ppoi', null=True, blank=True)
    back_photo = VersatileImageField(upload_to='user/id/', ppoi_field='image_ppoi', null=True, blank=True)
    image_ppoi = PPOIField()
    user = models.ForeignKey(User, related_name='Id', on_delete=models.CASCADE)

