from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from time import sleep
import json,re,sys,os
import requests
from bs4 import BeautifulSoup
import subprocess
#creating new session
c = requests.Session()
print("""================================================================================
A Bot Developed By Ruthran Elangovan To automate process of a telegram Bot
Contact me on telegram my ID is: @iamsry
instagram: @ruthra_the_destroyer
website: will lanch soon....
=========================================================================================
     
Author By Ruthran Elangovan
Channel: Professorhulk
Supported By Knowledge❤️""")

print ("This bot is used to automate @BTC_Click_Bot")



ua={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"}
# to print remaining timing for website visit
def print_timer(x):
    sys.stdout.write("\r")
    sys.stdout.write("                                                               ")
    for remaining in range(x, 0, -1):
       sys.stdout.write("\r")
       sys.stdout.write("-->{:2d} seconds remaining".format(remaining))
       sys.stdout.flush()
       sleep(1)


api_id = 1529432 #Api ID
api_hash = 'cf416e154ed19428033b82b8ee741c77' # API HASH
phone_number = input("Enter your telegram mobile number with country code:")

client = TelegramClient("session/"+phone_number, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
  try:
    client.send_code_request(phone_number)
    me = client.sign_in(phone_number, input('Enter Your Code : '))
  except SessionPasswordNeededError:
   passw = input("Your 2fa Password : ")
   me = client.start(phone_number,passw)
me = client.get_me()
print ("Username: ",me.username)#getting username
print ("----------Starting the Automation-----------!")
try:
 channel_entity=client.get_entity("@BitcoinClick_bot")
 channel_username="@BitcoinClick_bot"
 for i in range(100000000):
  sys.stdout.write("\r")
  sys.stdout.write("                                                              ")
  sys.stdout.write("\r")
  sys.stdout.write("-->Trying to Fetch URL:")
  sys.stdout.flush()
  client.send_message(entity=channel_entity,message="🖥 Visit sites")
  sleep(3)
  posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
  if posts.messages[0].message.find("Sorry, there are no new ads available") != -1:
     print ("\n-->Ads are not available try after some time!!!")
     client.send_message(entity=channel_entity,message="💰 Balance")
     sleep(5)
     posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
     message = posts.messages[0].message
     print ("-->",message)
     print("Retrying in 5 minutes")
     print("Press Ctrl+'C' to quit")
     sleep(300)
     
  else:
    try:
     url = posts.messages[0].reply_markup.rows[0].buttons[0].url
     sys.stdout.write("\r")
     sys.stdout.write("-->Visit "+url)
     sys.stdout.flush()
     id = posts.messages[0].id
     r = c.get(url, headers=ua, timeout=15, allow_redirects=True)
     soup = BeautifulSoup(r.content,"html.parser")
     if soup.find("div",class_="g-recaptcha") is None and soup.find('div', id="headbar") is None:
        sleep(2)
        posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
        message = posts.messages[0].message
        if posts.messages[0].message.find("You must stay") != -1 or posts.messages[0].message.find("Please stay on") != -1:
           sec = re.findall( r'([\d.]*\d+)', message)
           print_timer(int(sec[0]))
           sleep(1)
           posts = client(GetHistoryRequest(peer=channel_entity,limit=2,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
           messageres = posts.messages[1].message
           sleep(2)
           sys.stdout.write("-->"+messageres+"\n")

     elif soup.find('div', id="headbar") is not None:
        for dat in soup.find_all('div',class_="container-fluid"):
            code = dat.get('data-code')
            timer = dat.get('data-timer')
            token = dat.get('data-token')
            print_timer(int(timer))
            r = c.post("https://dogeclick.com/reward",data={"code":code,"token":token}, headers=ua, timeout=15, allow_redirects=True)
            js = json.loads(r.text)
            sys.stdout.write("-->You earned "+js['reward']+" BTC for visiting a site!\n")
     else:
        sys.stdout.write("\r")
        sys.stdout.write("                                                                ")
        sys.stdout.write("\r")
        sys.stdout.write("Captcha Detected")
        sys.stdout.flush()
        sleep(2)
        client(GetBotCallbackAnswerRequest(
        channel_username,
        id,
        data=posts.messages[0].reply_markup.rows[1].buttons[1].data
        ))
        sys.stdout.write("Skiping Captcha...!")
        sleep(2)
    except:
        sleep(3)
        posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
        message = posts.messages[0].message
        if posts.messages[0].message.find("You must stay") != -1 or posts.messages[0].message.find("Please stay on") != -1:
           sec = re.findall( r'([\d.]*\d+)', message)
           print_timer(int(sec[0]))
           sleep(1)
           posts = client(GetHistoryRequest(peer=channel_entity,limit=2,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
           messageres = posts.messages[1].message
           sleep(2)
           sys.stdout.write("-->"+messageres+"\n")

finally:
   client.disconnect()#Dissconnecting from client
