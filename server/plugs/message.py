from jmessage.message import Message, Model
from jmessage.user import User as JUser
from server.celery import app

from .conf import app_key, master_secret
import json
import time
import requests

class CJMessage(object):

    def __init__(self, app_key, master_secret):
        session = requests.Session()
        session.auth = (app_key, master_secret)
        self._session = session

    def get(self, uri, params=None):
        return self._session.get(uri, params=params)

    def post(self, uri, params=None, data=None, files=None):
        return self._session.post(uri, params=params, json=data, files=files)

    def put(self, uri, params=None, data=None):
        headers = { 'content-type': 'application/json; charset=utf-8' }
        return self._session.put(uri, params=params, json=data, headers=headers)

    def delete(self, uri, params=None, data=None):
        headers = { 'content-type': 'application/json; charset=utf-8' }
        return self._session.delete(uri, params=params, json=data, headers=headers)

_jmessage = CJMessage(app_key, master_secret)
# _jpush.set_logging("DEBUG")

@app.task()
def send_admin_message(content, target):
    modal = Model()
    modal.text(content)
    modal.set_target(target, 'single')
    modal.set_from('admin', 'admin')
    print(modal.json())
    Message(_jmessage).send(modal)

@app.task()
def update_password(username, password):
    if username is None or password is None:
        return
    print(username)
    print(password)
    JUser(_jmessage).update_password(username, password)

@app.task()
def delete_user(username):
    if username is None:
        return 
    JUser(_jmessage).delete(username)

@app.task()
def create_user(username, password):
    if username is None or password is None:
        return 
    JUser(_jmessage).create(username, password)
    