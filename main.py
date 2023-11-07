import evdev
import datetime
import time
import json
import warnings
from linebot import LineBotSdkDeprecatedIn30
from linebot import LineBotApi
from linebot.models import TextSendMessage


warnings.filterwarnings("ignore", category=LineBotSdkDeprecatedIn30)
with open('secret.json', 'r') as f:
    api = json.load(f)
    
bot_api = LineBotApi(api['access_token'])

while True:
    try:
        device = evdev.InputDevice('/dev/input/event2')
        now = datetime.datetime.now()
        print("["+now.strftime('%Y/%m/%d %H:%M:%S')+"] Connected:"+str(device))
        for event in device.read_loop():
            if event.type != evdev.ecodes.EV_KEY:
                continue
            if event.value != 1:
                continue
            if event.code == evdev.ecodes.KEY_VOLUMEUP:
                print("["+now.strftime('%Y/%m/%d %H:%M:%S')+"] 誰かが呼んでいます!!")
                user_id = api['userid']
                messages = TextSendMessage(text='誰かが呼んでいます!')
                bot_api.push_message(user_id, messages=messages)
                time.sleep(5)
                break
    except Exception as e:
        time.sleep(3)

