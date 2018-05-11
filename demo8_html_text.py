#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
一个HTML文件，找出里面的正文。
1) python3 中不再支持urllib2 模块，urllib2中的方法 需要通过urllib.request 来访问
2）当使用urllib.urlopen打开一个 https 链接时，会验证一次 SSL 证书，而当目标网站使用的是自签名的证书时就会抛出一个 urllib2.URLError
解决办法 ： https://blog.csdn.net/moonhillcity/article/details/52767999
3）print(urllib.request.urlopen("https://www.baidu.com/")) 输出： <http.client.HTTPResponse object at 0x103281400>


参考文档：https://www.cnblogs.com/my1e3/p/6622306.html （网页解析器分析）
https://blog.csdn.net/DoJintian/article/details/51382615


'''


# 方法1：使用urllib.request库及re.findall()
import re
import urllib.request
import ssl
from bs4 import BeautifulSoup

# ssl._create_default_https_context = ssl._create_unverified_context
# url = 'https://www.baidu.com/'
# data=urllib.request.urlopen(url) #<http.client.HTTPResponse object at 0x10ab11080>
# text= data.read().decode()
# print(text)
#
# body = re.findall(r'<body>[\s\S]*</body>',text)
# print(body)



#方法2 ：通过urllib.request打开html网页 并转化为string类型，BeautifulSoup（）方法
import re
import urllib.request
import ssl
from bs4 import BeautifulSoup

# ssl._create_default_https_context = ssl._create_unverified_context
# url = 'http://linyii.com'
# data=urllib.request.urlopen(url) #<http.client.HTTPResponse object at 0x10ab11080>
# text= data.read().decode()
# print(text)
#
# print("---------------")
# soup = BeautifulSoup(text,'html.parser') #text 为带解析文本，html.parser为解析器
# print(soup.text)



#方法3：将html文档直接拷贝出来而非通过urllib.request打开，解析

html_doc = """
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

soup = BeautifulSoup(html_doc,'lxml')#如果不加入lxml，会提示错误
print(soup.text)



# from bs4 import BeautifulSoup
# import urllib.request
# url = 'http://www.ruanyifeng.com/blog/2015/05/thunk.html'
# data= urllib.request.urlopen(url).read().decode()
#
# soup = BeautifulSoup(data,'lxml')
# #查找标签节点
# print(soup.find_all('a')) #返回所有的节点list
# print(soup.find('a')) #返回第一个节点
# print('------------')
#
# #查找节点属性
# print(soup.find_all('a',href='http://www.ruanyifeng.com/blog/2015/04/generator.html'))
# print(soup.find('a',title="订阅Feed"))
# print(soup.name)
# #print(soup.text)
# print('------------')
# #print(soup.get_text())

