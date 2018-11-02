#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os

# path=r"/Users/user/Desktop/1025"
#
# file=os.listdir(path)
# print(file)


#
# import datetime,string
#
# print(datetime.datetime.now().strftime('%Y-%m-%d'))


li=[]
for x in range(5):
    li.append(lambda x: x*2)
    print(li)