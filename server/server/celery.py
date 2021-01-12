from __future__ import absolute_import
 
import os
import time
 
from celery import Celery
 
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings.dev')
 
from django.conf import settings  # noqa
 
app = Celery('server')
 
# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task
def add(x, y):
    time.sleep(5)
    return x + y