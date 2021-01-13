from jmessage import JMessage
from jmessage.message import Message, Model
from jmessage.user import User as JUser
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
    print(modal.json())
    Message(_jmessage).send(modal)

@app.task()
def update_password(username, password):
    print(username, password)
    JUser(_jmessage).update_password(username, password)

@app.task()
def delete_user(username):
    JUser(_jmessage).delete(username)

@app.task()
def create_user(username, password):
    JUser(_jmessage).create(username, password)
    