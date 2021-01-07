from .conf import app_key, master_secret
import jpush

_jpush = jpush.JPush(app_key, master_secret)
# _jpush.set_logging("DEBUG")

def send_message(alias, title, body=None):
    push = _jpush.create_push()
    push.audience = jpush.audience(
        jpush.alias(alias)
    )
    push.options = {
         "apns_production": False
    }
    push.notification = jpush.notification(alert={
        "title": title,
        "body": body
    }, android={
        "badge": "+1",
        "extras": {
            "android-key1": "android-value1"
        }
    }, ios={
        "sound": "sound.caf",
        "badge": "+1",
        "extras": {
            "ios-key1": "ios-value1"
        }
    })
    push.platform = jpush.all_
    try:
        response=push.send()
    except jpush.common.Unauthorized:
        raise jpush.common.Unauthorized("Unauthorized")
    except jpush.common.APIConnectionException:
        raise jpush.common.APIConnectionException("conn")
    except jpush.common.JPushFailure:
        print ("JPushFailure")
    except:
        print ("Exception")