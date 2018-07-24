#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# -*- coding: UTF-8 -*-
import requests
import random
import string
import re
import sys
import datetime
reload(sys)
sys.setdefaultencoding( "utf-8" )

def kanjia():
    url="http://promotion-api.vip.elong.com/promotionapi/promotiondiscount/getcash?"
    activityid="2c65e41f-f970-41a4-8d05-c157619998ba"
    openid="o498X0QCMjyJsoDLWbMGhdO"
    workfile=open('kanjiafile.txt','ab+')
    #测试次数
    testnum=18
    #初始定义
    i=1
    while i <= testnum :
        s1=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
        i+=1
        newopenid=openid+s1
        urls=url+"activityId="+activityid+"&"+"openId="+newopenid
        #print(urls)
        date={'activityiId':activityid , 'openId':newopenid }
        #print(date)
        s=requests.get(urls)
        # print(s.text)
        #print(u"中文"+str(s.text))
        texts=s.json()
        nowtime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #print(texts['ErrorMessage'])
        if texts['ErrorMessage']=='很遗憾，您未中奖~':
            writes="微信风控原因:"+'\t'+str(s.text)+'\t'+"openid:"+newopenid +nowtime
            print(writes)
        if texts['ErrorMessage']=='很抱歉，您没有中奖~':
            writes="数量达到上限了"+'\t'+str(s.text)+'\t'+"openid:"+newopenid
            print(writes)
        if texts['ErrorMessage']=='很抱歉，您未中奖~':
            writes="酒店风控原因"+'\t'+str(s.text)+'\t'+"openid:"+newopenid
            print(writes)
        if texts['ErrorMessage']=='很遗憾，您没有中奖~':
            writes="概率问题导致"+'\t'+str(s.text)+'\t'+"openid:"+newopenid
            print(writes)
        workfile.write(writes+"\n")
if __name__ == '__main__':
    kanjia()