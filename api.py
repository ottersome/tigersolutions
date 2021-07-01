import os

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
    MessageEvent, TextMessage, TextSendMessage,
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
    line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="3q for your message")
    )
    #with open(os.path.abspath("maskdata.csv"), newline='') as csvfile:
    #    rows = csv.reader(csvfile, delimiter=',')
    #    for row in rows:
    #        rows_list.append(row)

    #line_bot_api.reply_message(
    #    event.reply_token,
    #    TextSendMessage(text=str(rows_list[number]))
    #)


if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=10420, debug=True,ssl_context='adhoc')
    app.run(host='0.0.0.0', port=10420, debug=True)
    #app.run(host='127.0.0.1', port=10420, debug=True)
