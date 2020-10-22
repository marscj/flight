from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from versatileimagefield.fields import VersatileImageField, PPOIField

class Department(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        db_table = 'department'
        
class User(AbstractUser):

    class Role(models.IntegerChoices):
        Staff = 0
        Admin = 1
        SupserAdmin = 2

    # 角色
    role = models.IntegerField(blank=True, null=True, choices=Role.choices, default=Role.Staff)

    # 头像
    avatar = VersatileImageField(upload_to='user/avatar/', ppoi_field='image_ppoi', null=True, blank=True)
    
    image_ppoi = PPOIField()

    class Meta:
        db_table = 'user'

