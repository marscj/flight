from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from versatileimagefield.fields import VersatileImageField, PPOIField

class Department(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        db_table = 'department'
        
class User(AbstractUser):

    class Role(models.IntegerChoices):
        User = 0
        Admin = 1

    # 护照类型
    possport_type = models.CharField(blank=True, null=True, max_length=4)

    # 国家码
    passport_code = models.CharField(blank=True, null=True, max_length=4)

    # 护照号码
    passport_no = models.CharField(blank=True, null=True, max_length=64)

    # 性别
    passport_sex = models.BooleanField(blank=True, null=True)

    # 国籍
    passport_nationality = models.CharField(blank=True, null=True, max_length=64)

    # 生日
    passport_date_birth = models.DateField(blank=True, null=True)

    # 出身地
    passport_place_birth = models.CharField(blank=True, null=True, max_length=64)

    # 签发日期
    passport_date_issue = models.DateField(blank=True, null=True)

    # 有效期
    passport_date_expiry = models.DateField(blank=True, null=True)

    # 签发机关
    passport_issuing_authority = models.CharField(blank=True, null=True, max_length=64)

    # 部门
    department = models.ForeignKey(Department, related_name='users', on_delete=models.SET_NULL, blank=True, null=True)

    # 角色
    role = models.IntegerField(blank=True, null=True, choices=Role.choices, default=Role.User)

    # 头像
    avatar = VersatileImageField(upload_to='user/avatar/', ppoi_field='image_ppoi', null=True, blank=True)
    
    image_ppoi = PPOIField()

    # 逻辑删除
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'

