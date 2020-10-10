from django.db import models

from user.models import User

class Apply(models.Model):

    remark = models.CharField(blank=True, null=True, max_length=256)
    
    author = models.ForeignKey(User, related_name='apply', on_delete=models.SET_NULL, blank=True, null=True)