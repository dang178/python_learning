#! /usr/bin/python3
# __*__ coding=utf-8 __*__

import requests,json,datetime,time
from wxpy import *
from bs4 import BeautifulSoup

def Wechat_login():
  bot = Bot(cache_path=True)
  chats= bot.chats()
  friends = bot.friends()
  groups = bot.groups()
  return bot

def GetWeather():
  rain_url = 'http://www.nmc.cn/f/rest/real/24hour/2019060415/58605'
  rain_map='http://image.nmc.cn/product/2019/06/03/STFC/medium/SEVP_NMC_STFC_SFER_ER1_ACHN_L88_PB_20190603180000000.jpg?v=1559587310704'
  response = requests.get(rain_url)
  if(response.status_code=requests.code.ok):
    return json.dumps(response.content)
  else :
    return 

def __main__():
    bot = Wechat_login()
    time = datetime.datetime.now()
    while(true):
        if(datetime.datetime.now()>time+datetime.timedelta(hours=1)):
            time = time+datetime.timedelta(hours=1)
            data = GetWeather()
            
        else:
            continue