from jmessage import JMessage
from jmessage.message import Message, Model
from celery import task

from .conf import app_key, master_secret
import json

_jmessage = JMessage(app_key, master_secret)
# _jpush.set_logging("DEBUG")

@task()
def send_message(content, target):
    message = Message(_jmessage)
    modal = Model()
    modal.text(content)
    modal.set_target(target, 'single')
    modal.set_from('admin', 'admin')
    
    try:
        print(modal.json())
        message.send(modal)
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)
