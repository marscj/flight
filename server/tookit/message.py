from jmessage import users
from jmessage import common
from conf import *

_jmessage = common.JMessage(app_key,master_secret)

def regist_user(username, password):
    users=jmessage.create_users()
    user= [users.build_user(username, password)]
    response=users.regist_user(user)

def send_message(title, **kwargs):

    messages=jmessage.create_messages()
    message=messages.build_message(1, "single" ,"admin","text", "xiaohuihui", "admin", "Hello, JMessage!")
    response=messages.send_messages(message)