import time
import requests
import os
import pause
from dotenv import load_dotenv

load_dotenv() 

bot_token = os.getenv('B_T')
user1 = os.getenv('U1')
user2 = os.getenv('U2')

count=0

def final_send(st):
    reponse = requests.get(st)
    return reponse.json()
    
def telegram_bot_sendtext(bot_message, model, bot_chatID, ct): 
    if model =='3' and bot_message!='404/403':
        send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
        '&parse_mode=MarkdownV2&text='+ bot_message + '%2C%20Model%203%2C%20count%20' + ct
        return final_send(send_text)
        print("1")

    elif model == 'y' and bot_message!='404/403':
        send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
        '&parse_mode=MarkdownV2&text='+ bot_message + '%2C%20Model%20Y%2C%20count%20' + ct
        return final_send(send_text)
        print("2")

    elif model == 'homepage' and bot_message!='404/403':
        send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
        '&parse_mode=MarkdownV2&text='+ bot_message + '%2C%20HomePage%2C%20count%20' + ct
        return final_send(send_text)
        print("3")
    else:
        return 0

def response_check(r):
    if r == 404 or r == 403:
        return '404%2F403'
    else:
        return 'Check%20Website%20ASAP'

while count<69:
          
    count+=1
    print("Count = ",count)

    response1 = requests.get("https://www.tesla.com/en_IN/model3/design#overview")
    print(response1.status_code)

    response2 = requests.get("https://www.tesla.com/en_IN/modely/design#overview")
    print(response2.status_code)

    response3 = requests.get("https://www.tesla.com/en_IN")
    print(response3.status_code)

    r1=response_check(response1.status_code)
    r2=response_check(response2.status_code)
    r3=response_check(response3.status_code)

    telegram_bot_sendtext(r1,'3',user1,str(count))
    telegram_bot_sendtext(r1,'3',user2,str(count))
    
    telegram_bot_sendtext(r2,'y',user1,str(count))
    telegram_bot_sendtext(r2,'y',user2,str(count))
    
    telegram_bot_sendtext(r3,'homepage',user1,str(count))
    telegram_bot_sendtext(r3,'homepage',user2,str(count))

    del response1, response2, response3, r1, r2, r3

    if count<10:
        pause.minutes(1)
    else:
        pause.minutes(25)
    
    if count==65:
        count=10
    
