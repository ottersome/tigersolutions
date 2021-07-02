# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 14:21:19 2021

@author: Eduin Hernandez
"""
import json

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
        
    flex = {"type": "flex",
            "altText": "Testing",
            "contents": bubble}
    
    return flex

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
if __name__ == '__main__':
    s0 = json.dumps(flex_notification_message(["Hello", "Welcome!"]))
    s1 = json.dumps(flex_notification_message(["It is very likely that your symptoms are caused by your medication!"], "Symptoms and Medication"))
    s2 = json.dumps(flex_notification_message(["Drowsiness", "Dry mouth", "Unsteadiness"], "Common Side-Effects from Medication"))
