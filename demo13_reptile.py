#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)
'''


import urllib.request
from bs4 import BeautifulSoup
import re
import os

url='http://tieba.baidu.com/p/2166231880'
content=urllib.request.urlopen(url).read().decode()

#print(content)

soup=BeautifulSoup(content,'lxml')

#print(soup.prettify())  #按照标准的缩进格式输出

#print(soup.find_all('div',class_='d_post_content j_d_post_content clearfix'))

img_list=soup.find_all('img',class_='BDE_Image')
print(len(img_list))
for img in img_list:
    #print(re.findall(r'src="(\S*)"',str(i)))
    # print(type(img))  #<class 'bs4.element.Tag'>
    #print(img.attrs)  #{'pic_type': '0', 'class': ['BDE_Image'], 'src': 'http://imgsrc.baidu.com/fo...
    # print(os.path.split(img['src'])[0]) #http://imgsrc.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C302%3Bap%3D%C9%BC%B1%BE%D3%D0%C3%C0%B0%C9%2C90%2C310/sign=8800a2e3b3119313c743ffb855036fa7
    # print(os.path.split(img['src'])[1]) #1e29460fd9f9d72abb1a7c3cd52a2834349bbb7e.jpg
    #print(img['src'])
    # with open('/Users/user/Documents/0013/'+os.path.split(img['src'])[1],'wb') as f:
    #     f.write(urllib.request.urlopen(img['src']).read())

    #print(type(img['src']))  #<class 'str'>
    # print(type(urllib.request.urlopen(img['src'])))  #<class 'http.client.HTTPResponse'>
    # print(type(urllib.request.urlopen(img['src']).read())) #<class 'bytes'>

    print(urllib.request.urlopen(img['src']).read()) #b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00d\x00d\x00\x00\xff\xdb\x00C\x00\x06\x04\
    print()
    print(img['src'].encode()) #b'http://imgsrc.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C390%3Bap%3D%C9%BC%B1%BE











# div_list=soup.find_all('div',class_='d_post_content j_d_post_content clearfix')
# print(len(div_list))
# #print(div_list)
# for div in div_list:
#     #print(json.loads(div.decode()))
#     #print(re.findall(r'src="(\S*)"',str(div)))
#     print(re.findall(r'img .* src="(.+?\.jpg)"',str(div)))





#print(''.join(div_list)) #这里是有join（）方法企图将list 连接为字符串的时候 报错，TypeError: sequence item 0: expected str instance, Tag found
#
# img_list=[]
# for div in div_list:
#     print(div)
#     #print(type(div)) #<class 'bs4.element.Tag'>
#     # soup_div=BeautifulSoup(div,'lxml')
#     # img_list=soup_div.find_all('img')
#     # print(img_list['src'])
#     for i in div:
#         img_list_i=re.findall(r'img .* src="(.+?\.jpg)"',str(i))
#         #print(img_list_i)
#         img_list.append(img_list_i)
#
#
# print(img_list)
#
# for i in img_list:
#     print(i)
#
# #urllib.request.urlretrieve()










# list=['1','a','c']
# print(''.join(list))

import re
# regx = re.compile("abc")
# print(type(regx))
# m11 = re.match(regx,"abcdefg")
# print(m11.group())



html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# import re
# soup=BeautifulSoup(html,'lxml')
# #print(soup.prettify())
#
# p_list=soup.find_all('p',class_="story")
# #print(p_list)
#
# #print(type(p_list[0])) #<class 'bs4.element.Tag'>
# print(p_list[0])
#
# print(re.findall(r'href="(\S*)"',str(p_list[0])))
# print(re.findall(r'href="\S*"',str(p_list[0])))
# print(re.findall(r'href="(\S)*"',str(p_list[0])))