#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itchat, time
import datetime as dt
from apscheduler.schedulers.background import BackgroundScheduler
import random


# 一些备选问候语
greetList = ['快去睡觉别熬夜','好好找工作加油','注意身体多喝热水','想你了求自拍']

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    msg.user.send("亲爱的别婉如,爱你哟")

def tick():
    users = itchat.search_friends(name=u'别婉如')
    print(users)
    userName = users[0]['UserName']
    print(userName)
    meetDate = dt.date(2017,1,26)
    now = dt.datetime.now()     # 现在的时间
    nowDate = dt.date.today()  # 今天的日期
    passDates = (nowDate-meetDate).days # 你跟你女朋友认识的天数
    print(passDates)
    itchat.send(u'今天是我们认识第%d天，%s,晚安'%(passDates,random.sample(greetList,1)[0]),toUserName=userName) # 发送问候语给女朋友
    nextTickTime = now + dt.timedelta(days=1)
    nextTickTime = nextTickTime.strftime("%Y-%m-%d 00:00:00")
    my_scheduler(nextTickTime)


def my_scheduler(run_time):
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, 'date', run_date=run_time)
    scheduler.start()

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    print(itchat.search_friends())

    users = itchat.search_friends(name=u'FZ')
    userName = users[0]['UserName']
    itchat.send('hello, filehelper', toUserName=userName)

    itchat.run()
    # itchat.logout()

    # itchat.auto_login(enableCmdQR=True)
    # itchat.auto_login(hotReload=True)

    # users = itchat.search_friends(name=u'别婉如')
    # print(users)
    # userName = users[0]['UserName']
    # print(userName)

    # now = dt.datetime.now()
    # print(now)
    # nextTickTime = now + dt.timedelta(days=1)
    # nextTickTime = nextTickTime.strftime("%Y-%m-%d 23:42:00")
    # my_scheduler(nextTickTime)
    # itchat.run()
