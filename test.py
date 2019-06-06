#! /usr/bin/python3
# __*__ coding=utf-8 __*__

import requests,json,datetime,time
from wxpy import *
from bs4 import BeautifulSoup
import xlwt

def Wechat_login():
  bot = Bot(cache_path=True)
  chats= bot.chats()
  friends = bot.friends()
  groups = bot.groups()
  return bot

def GetAQI():
  mainURL = 'http://www.pm25.in/nanchang'
  response = requests.get(mainURL)
  return str(response.content,encoding='utf-8')

def parser(content):
  soup = BeautifulSoup(content,features='html.parser')
  ## 明细
  # rows = soup.findAll('tr')
  # datas=[]
  # for row in rows:
  #   row=row.findChildren()
  #   data = []
  #   for column in row:
  #     data.append(column.next)
  #   datas.append(data)
  # return datas
  level = soup.find('div',attrs={'class':'level'}).findChildren()[0].next
  captions = soup.findAll('div',attrs={'class':'caption'})
  values = soup.findAll('div',attrs={'class':'value'})
  strmsg = "南昌空气质量情况:{},".format(level)
  for i in range(0,len(captions)):
    strmsg+="{}值为{}".format(captions[i].next,values[i].next)
  return strmsg.replace('\n','').replace(' ','')

def FillExcel(datas):
  wbk = xlwt.Workbook(encoding='utf-8')
  sheet = wbk.add_sheet('realtime_AQI',cell_overwrite_ok=True)
  for i in range(0,len(datas)):
    for j in range(0,len(datas[i])):
      sheet.write(i,j,datas[i][j])
  wbk.save('realtimeAQI_{}.xls'.format(datetime.datetime.now().strftime('%Y%m%d%H%M')))


bot = Wechat_login()

kd=ensure_one(bot.friends().search('kd'))
while(True):
  content = GetAQI()
  msg = parser(content)
  kd.send('当前时间：{}，{}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),msg))
  time.sleep(60*60)


