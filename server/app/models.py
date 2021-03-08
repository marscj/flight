import uuid
from django.db import models
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver

class App(models.Model):
    
    class Type(models.TextChoices):
        IOS = 'Ios'
        ANDROID = 'Android'

    type = models.CharField(choices=Type.choices, default=Type.ANDROID, max_length=16)

    name = models.CharField(blank=True, null=True, max_length=64)

    version = models.CharField(blank=True, null=True, max_length=64)

    code = models.CharField(blank=True, null=True, max_length=16)

    file = models.FileField(upload_to='uploads/app/', blank=True, null=True)

    redirect = models.URLField(blank=True, null=True)

    enable_redirect = models.BooleanField(default=False)

    #请求返回码
    code = models.IntegerField(default=200)

    #请求错误信息
    msg = models.TextField(blank=True, null=True)

    #更新的状态
    # 0:无版本更新
    # 1:有版本更新，不需要强制升级
    # 2:有版本更新，需要强制升级
    updateStatus = models.IntegerField(default=0)

    #最新版本号[根据版本号来判别是否需要升级]
    versionCode = models.IntegerField(blank=True, null=True)

    #最新APP版本的名称[用于展示的版本名]
    versionName = models.TextField(blank=True, null=True)

    #APP更新时间
    uploadTime = models.DateField(auto_now_add=True)

    #APP变更的内容
    modifyContent = models.TextField(blank=True, null=True)

    downloadUrl = models.URLField(blank=True, null=True)

    apkMd5 = models.UUIDField(default=uuid.uuid4, editable=False)

    apkSize = models.IntegerField(default=49152)

@receiver(pre_delete, sender=App)
def app_pre_delete(sender, instance, **kwargs):
    
    if instance.file is not None: 
        instance.file.delete()