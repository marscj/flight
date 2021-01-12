from jmessage import JMessage
from jmessage.message import Message, Model
from jmessage.user import User
from server.celery import app

from .conf import app_key, master_secret
import json
import time
import requests

_jmessage = JMessage(app_key, master_secret)
# _jpush.set_logging("DEBUG")

@app.task()
def send_message(content, target):
    modal = Model()
    modal.text(content)
    modal.set_target(target, 'single')
    modal.set_from('admin', 'admin')
    Message(_jmessage).send(modal)

@app.task()
def update_password(self, username, password):
    User(_jmessage).update_password(username, password)

@app.task()
def delete(self, usernames):
    User(_jmessage).delete(username)

@app.task()
def create(self, username, password,
        nickname=None, avatar=None, birthday=None, signature=None, gender=None, region=None, address=None, extras=None, admin=False):
    User(_jmessage).create()
    