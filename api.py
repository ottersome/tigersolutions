import os
import json


if os.getenv('DEVELOPMENT') is not None:
    from dotenv import load_dotenv

    load_dotenv(dotenv_path='../.env')

import sys

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)



<<<<<<< Updated upstream
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage, LocationSendMessage,
    VideoSendMessage, ImageSendMessage, StickerSendMessage,
)

from linebot.models import (
=======
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage, LocationSendMessage,
    VideoSendMessage, ImageSendMessage, StickerSendMessage,
)

from linebot.models import (
>>>>>>> Stashed changes
    MessageEvent, TextMessage, TextSendMessage, QuickReply, QuickReplyButton, MessageAction,
    DatetimePickerAction, URIAction, CameraAction, CameraRollAction, LocationAction,
    PostbackAction,
)

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET') or '69d79bf3b4be8fad2500c0a1caa4886f'
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN') or 'Fo+7x9K1NusGG1G8q0vI91+7X/ofQidNL8CTEkgHIUmzSjIZyl7hdQ1Y0N2Bzga3uvAjbIEPHVEfFcCyyJ5phxaNhjvXiRFhsu7dO8sp6XF8DJqNam3OsVesofnyk8HdMLnrjr41zjdAHZ3UJWzdaAdB04t89/1O/w1cDnyilFU='
print(channel_secret)
print(channel_access_token)

if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# CSV Example
import csv


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    print("Got message : "+event.message.text)
    #number = int(event.message.text)
    #rows_list = []
    print('Message received')
    if event.message.text == 'Location':
        print('inside if Location')
        quick_reply = QuickReply(
        items=[
            # QuickReplyButton(action=MessageAction(label="Hello", text="World")),
            # QuickReplyButton(action=DatetimePickerAction(
            #     label="Time",
            #     data="storeId=12345",
            #     mode="datetime",)),
            # QuickReplyButton(action=CameraAction(label="Camera")),
            # QuickReplyButton(action=CameraRollAction(label="Camera Roll")),
            QuickReplyButton(action=LocationAction(label="Set Location✍️")),
            QuickReplyButton(action=MessageAction(label="No", text="I am so sorry."))

        ])
<<<<<<< Updated upstream
=======
        

>>>>>>> Stashed changes
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text, quick_reply=quick_reply)
        )
        
        # output = LocationSendMessage(
        #     title = 'My location',
        #     address = 'Position')
            
            
            
<<<<<<< Updated upstream
            
=======
    s0 = json.dumps(flex_notification_message(["Hello", "Welcome!"]))
    s1 = json.dumps(flex_notification_message(["It is very likely that your symptoms are caused by your medication!"], "Symptoms and Medication"))
    s2 = json.dumps(flex_notification_message(["Drowsiness", "Dry mouth", "Unsteadiness"], "Common Side-Effects from Medication"))
>>>>>>> Stashed changes
    line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="testo")
    )
    #with open(os.path.abspath("maskdata.csv"), newline='') as csvfile:
    #    rows = csv.reader(csvfile, delimiter=',')
    #    for row in rows:
    #        rows_list.append(row)

    #line_bot_api.reply_message(
    #    event.reply_token,
    #    TextSendMessage(text=str(rows_list[number]))
    #)

"Template for sending a flex message"

'Normal message - Use this when providing an answer to user'
def flex_notification_message(text: list, title:str = "" , titleBackgroundColor:str = "#00B900"):
    content = []
    if type(text) == list:
        for i0 in text:
            content.append({"type": "text",
                            "text": i0,
                            "wrap": True
                            })
    else:
        content.append({"type": "text",
                       "text": i0,
                       "wrap": True
                       })
    bubble = {
          "type": "bubble",
          "body": {
            "type": "box",
            "layout": "vertical",
            "contents": content
          },
           "styles": {
             "header": {
               "backgroundColor": titleBackgroundColor
             }
           }
         }
    if(len(title)>0):
        bubble["header"] = {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": title,
                "wrap": True,
                "color": "#FFFFFF",
                "weight": "bold"
              }
            ]
          }
    
    return bubble

'To modify'
# def create_bubble():
    
#     bubble = {
#       "type": "bubble",
#       "body": {
#         "type": "box",
#         "layout": "vertical",
#         "contents": []
#       }
#     }
    
#     return bubble

'To modify'
# def add_content(content):
#     flex = {
#       "type": "carousel",
#       "contents": content
#     }

#     return flex
# if __name__ == '__main__':
   

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=10420, debug=True,ssl_context='adhoc')
    app.run(host='0.0.0.0', port=10420, debug=True)
    #app.run(host='127.0.0.1', port=10420, debug=True)
