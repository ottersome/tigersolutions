import os
import json
import csv
import 

parentWebsites = [\
        "http://www.sciencedaily.com/news/health_medicine/infectious_diseases/",
        ]

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

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, QuickReply, QuickReplyButton, MessageAction,
    DatetimePickerAction, URIAction, CameraAction, CameraRollAction, LocationAction,
    PostbackAction, LocationMessage, FlexSendMessage
)

from SideEffect.fullse_dict_create import name_se_dic as nsd
from Kaggle.drugsCom import df
from flex_messages.flex_function import flex_notification_message

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET') or 'LINE_CHANNEL_SECRET'
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN') or 'LINE_CHANNEL_ACCESS_TOKEN'
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

symptom_keys = []

@handler.add(MessageEvent, message=LocationMessage)
def message_location(event):
    print("Location was provided")
    print("Got message:", event.message.address) 
    print("Longitude and Latitude", event.message.longitude, " x " , event.message.latitude)
    scrappy = Scraper(event.message.address\
            ,["fever","nausea"],parentWebsites)
    scrappy.organizeList()
    stringSymp = str(symptom_keys)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="Your location is: " + event.message.address +\
                "\nAnd your symptoms are : " + stringSymp

            ))
    
@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    print("Got message : " + event.message.text)
    print('Message received\n\n')
    key_message = str(event.message.text).lower()
    key_splitted = key_message.split()
    #if 'location' in key_message:
    #    quick_reply = QuickReply(
    #    items=[
    #        QuickReplyButton(action=LocationAction(label="Set Location✍️")),
    #        QuickReplyButton(action=MessageAction(label="No", text="No"))

    #    ])
    #    
    #    line_bot_api.reply_message(
    #        event.reply_token,
    #        TextSendMessage(text=event.message.text, quick_reply=quick_reply)
    #    )
    #elif 'symptom' in key_message and 'medicine' in key_message:
    if 'symptom' in key_message and 'medicine' in key_message:
        symptom_count = 0
        medicine_count = 0
        
        for m0, i0 in zip(key_splitted, range(len(key_splitted))):
            if m0 == 'symptom':
                symptom_count = i0
            if m0 == 'medicine':
                medicine_count = i0
        
        symptom_keys = key_splitted[(symptom_count + 1): medicine_count]
        medicine_keys = key_splitted[(medicine_count + 1):]
        
        
        if(medicine_keys[0] in nsd):
            listings = nsd[medicine_keys[0]]
            listings = " ".join(listings).lower()
            count = len(symptom_keys)
            count_max = len(symptom_keys)
            
            for m0 in symptom_keys:
                if(m0 in listings):
                    count -= 1
            if count == 0:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="It is very likely the symptoms you are having are cause by your medication."))
            elif count < count_max:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="Some of your symptoms align with the side-effect of your medication."))
            else:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="Your symptoms are not caused by your medication!"))
            
            'Provide the option to search in vicinity - Symptom keys is global list of string variable'
        
    elif 'symptom' in key_message and 'location' in key_message:
                
        else:
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Medicine not found"))
    elif 'medicine' in key_message:
        medicine_count = 0
        
        for m0, i0 in zip(key_splitted, range(len(key_splitted))):
            if m0 == 'medicine':
                medicine_count = i0
        
        medicine_keys = key_splitted[(medicine_count + 1):]
        if(medicine_keys[0] in nsd):
        
            listings = nsd[medicine_keys[0]]
            
            if(len(listings)>2):
                listings[-1] =  'and ' + listings[-1]
                listings = ", ".join(listings).lower()
    
            elif(len(listings)>1):
                listings = " and ".join(listings).lower()
            else:
                listings = str(listings[0])
            
            df_temp = df[df['drugName'].isin([medicine_keys[0].capitalize()])].sort_values(by=['rating'], ascending=False).review.head(15).tolist()
            
            temp_str = "\n\nReviews:"
            for d0 in df_temp:
                print("Reviews: ", d0)
                print("\n")
                if(len(d0) < 100):
                    # print("Reviews: ", d0)
                    # line_bot_api.message(
                    # event.reply_token,
                    # TextSendMessage(text="Reviews: "  + d0))
                    temp_str += "\n" + d0 + "\n"
                    
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="List of Side-Effects include: "  + listings + "." + temp_str))
            
            
        else:
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Medicine not found"))
    elif 'symptom' in key_message:
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="Please also provide your medications!")
        )
        
        'Provide the option to search in vicinity - Symptom keys is global list of string variable'
    elif 'no' in key_message:
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="Okay")
        )
    elif event.message.text == 'flex':
        'Test Flex'
    else:
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="No Comment")
        )
   

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=10420, debug=True,ssl_context='adhoc')
    app.run(host='0.0.0.0', port=10420, debug=True)
    #app.run(host='127.0.0.1', port=10420, debug=True)

