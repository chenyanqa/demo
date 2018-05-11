#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
题目：一个HTML文件，找出里面的链接。

'''

html1="""
<html><head><title>The Dormouse's story</title></head> 
<body> 
<p class="title"><b>The Dormouse's story</b></p> 
 
<p class="story">Once upon a time there were three little sisters; and their names were 
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>, 
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; 
and they lived at the bottom of a well.</p> 
 
<p class="story">...</p> 
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html1,'lxml')
text = soup.get_text()  #获取html正文内容
print(text)

linkslist = soup.find_all('a') #获取html中 所以连接列表

# for i in linkslist:  #简单打印所有的links
#     print(i)


for link in linkslist:
    print(link.name,link['href'],link['id'],link.get_text())





