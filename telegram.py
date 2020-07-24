#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 10:59:22 2019

@author: alexliu
"""

import telegram

#可以修改机器人的token
bot = telegram.Bot(token='')

#发送的内容
context =  """
hello world!
"""

for i in range(0,len(bot.getUpdates())):
    chat_id = bot.getUpdates()[i].message.chat_id
    print("========发送给"+ str(chat_id) + "========")
    try:
        bot.send_message(chat_id=chat_id,text=context)
    except:
        bot.send_message(chat_id=chat_id,text=context)

print("===========Done!!!==============")