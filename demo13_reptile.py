#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)

 1、python2中的urllib2库 在python3中已经不用了，而是使用urllib.request替代

'''


import urllib.request
from bs4 import BeautifulSoup
import re
import os

# url='http://tieba.baidu.com/p/2166231880'
# content=urllib.request.urlopen(url).read().decode()
#
# #print(content) #差不多是 在chrome检查网页时 所看到的内容，但是是非标准格式
#
# soup=BeautifulSoup(content,'lxml')  #将待解析的content（html格式），按照'lxml'解释器进行解析
#
# #print(soup)  #其实跟 直接打印content差不多
# #print(soup.prettify())  #按照标准的缩进格式输出
# #print(soup.find_all('div',class_='d_post_content j_d_post_content clearfix')) #这个是按照比较外层的div去检索，然后还需要在去检索去img-list
#
# img_list=soup.find_all('img',class_='BDE_Image')  #查找的时候  最好直接找最里层的内容（soup.find_all（）方法只要是tag即'<' 或者<>，都能够被检索，不管是在外城还是内层）
# print(len(img_list))
# i=0
# for img in img_list:
#     #print(re.findall(r'src="(\S*)"',str(i)))
#     #print(type(img))  #<class 'bs4.element.Tag'>
#     #print(img.attrs)  #{'pic_type': '0', 'class': ['BDE_Image'], 'src': 'http://imgsrc.baidu.com/fo...
#     #print(os.path.split(img['src'])[0]) #http://imgsrc.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C302%3Bap%3D%C9%BC%B1%BE%D3%D0%C3%C0%B0%C9%2C90%2C310/sign=8800a2e3b3119313c743ffb855036fa7
#     #print(os.path.split(img['src'])[1]) #1e29460fd9f9d72abb1a7c3cd52a2834349bbb7e.jpg
#     #print(img['src'])
#     '''
#     方法1：使用with open(path，'wb'）as f：
#                 f.write()  去写入文件
#     '''
#     # with open('/Users/user/Documents/0013/'+os.path.split(img['src'])[1],'wb') as f:
#     #     f.write(urllib.request.urlopen(img['src']).read())
#
#     # print(type(img['src']))  #<class 'str'>
#     # print(type(urllib.request.urlopen(img['src'])))  #<class 'http.client.HTTPResponse'>
#     # print(type(urllib.request.urlopen(img['src']).read())) #<class 'bytes'> ，因为网络的东西 都是使用比特流的形式传递的，所以直接read（）出来的内容是ibytes，需要decode（）变成str
#     #
#     # print(urllib.request.urlopen(img['src']).read()) #b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00d\x00d\x00\x00\xff\xdb\x00C\x00\x06\x04\
#     # print()
#     # print(img['src'].encode()) #b'http://imgsrc.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C390%3Bap%3D%C9%BC%B1%BE
#
#     '''
#         方法2：使用urlretrieve(url, filename=None, reporthook=None, data=None)方法，取回一个url返回的所有内容并临时保存起来
#     '''
#     #print(type(os.path.split(img['src']))) #<class 'tuple'>
#     #print(os.path.split(img['src'])[1]) #1e29460fd9f9d72abb1a7c3cd52a2834349bbb7e.jpg
#     print(img['src'])
#     #urllib.request.urlretrieve(img['src'],'/Users/user/Documents/0014/'+os.path.split(img['src'][1])) #这个语句错误的原因时因为[1]的位置不对
#
#     #urllib.request.urlretrieve(img['src'], '/Users/user/Documents/0014/'+os.path.split(img['src'])[1])
#
#     urllib.request.urlretrieve(img['src'], '/Users/user/Documents/0014/'+'%s.jpg'%(i))
#     i=i+1



'''
这里由于使用soup.find_all（）方法时，从div层开始找的，所以找出来一个div的list ，但是还需要再冲div list 里面检索出img list 非常费时，所以
最好从一开始的时候 就从img 开始检索，这样的话 后续可以直接img的attrs 检索出对应的属性值
'''
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
#
# str='a bc'
# print(str.split(' '))


import re
# regx = re.compile("abc")
# print(type(regx))
# m11 = re.match(regx,"abcdefg")
# print(m11.group())

'''
样例html 分析：
'''
#
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie1" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie2" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie3" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
#
# import re
# soup=BeautifulSoup(html,'lxml')
# #print(soup.prettify())
#
# p_list=soup.find_all('p',class_="story")
# #print(p_list)
#
# #print(type(p_list[0])) #<class 'bs4.element.Tag'>
# print(type(p_list[0]))  #<class 'bs4.element.Tag'>
#
# print(str(p_list[0]))
# '''
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a class="sister" href="http://example.com/elsie1" id="link1"><!-- Elsie --></a>,
# <a class="sister" href="http://example.com/lacie2" id="link2">Lacie</a> and
# <a class="sister" href="http://example.com/tillie3" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# '''
#
# # print(re.findall(r'href="(\S*)"',str(p_list[0])))
# '''
# 匹配结果：['http://example.com/elsie', 'http://example.com/lacie', 'http://example.com/tillie']
# 解析："\S"表示 匹配任意非空白字符（空白字符是指 例如空格，换行，制表\t这些） ，"*" 表示匹配前一个字符0个或者多个，"（）"表示将括号里面
# 的内容作为一个分组，仅匹配括号里面的表达式
# '''
#
# # print(re.findall(r'href="\S*"',str(p_list[0])))
# '''
# 匹配结果：['href="http://example.com/elsie"', 'href="http://example.com/lacie"', 'href="http://example.com/tillie"']
# 解析：这里 没有加"（）"，则表示 匹配整个'href="\S*"'表达式，因此匹配结果中会带上 'href=。。。'
# '''
#
# #print(re.findall(r'href="(\S)*"',str(p_list[0])))
# '''
# 匹配结果：['1','2','3']
# 解析：这里r'href="(\S)*"' 表示仅匹\S 0个或者多个，一般不这么写
# '''
#
# print(re.findall(r'href="(.*)"',str(p_list[0])))
# '''
# 匹配结果：['http://example.com/elsie1" id="link1', 'http://example.com/lacie2" id="link2', 'http://example.com/tillie3" id="link3']
# 出现了 贪婪模式，他会尽可能多去的匹配字符，因此会把'id=。。'这些也给匹配上
# '''
#
# print(re.findall(r'href="(.*)"',str(p_list[0])))
# '''
# 匹配结果：['http://example.com/elsie1', 'http://example.com/lacie2', 'http://example.com/tillie3']
# 解析：这里'.' 表示除了换行符以为的任意字符（是能够匹配最对的字符），.*表示匹配除了换行符以外的字符 任意多个，所以会进入贪婪模式，
# 会匹配尽可能多的结果，但是加上一个 '？' 可以进入非贪婪模式，匹配最少的结果
# '''


import requests
from bs4 import BeautifulSoup

url='http://tieba.baidu.com/p/2166231880'
# content= urllib.request.urlopen(url)
# print(type(content))  #<class 'http.client.HTTPResponse'>
# print(content.read()) #读取出二进制内容
# print(content.geturl()) #取出本次实际访问的url，可以判断是否发生了重定向
# print(content.info()) #读取headers的信息
# print(content.getcode()) #获取本次url的状态码
#print(content.read().decode())
# soup=BeautifulSoup(content.read().decode(),'lxml')
# print(soup.prettify())

resp= requests.get(url)
# print(type(resp))  #<class 'requests.models.Response'>
# print(resp) #<Response [200]>
# print(resp.status_code)
# print(resp.encoding)
# print(resp.cookies)
# print(resp.content) #二进制的响应内容
# print(resp.text) #字符串式的响应内容
# print(resp.json) #<bound method Response.json of <Response [200]>>
# print(resp.raw) #<urllib3.response.HTTPResponse object at 0x10dfce128>

soup=BeautifulSoup(resp.text,'lxml')
print(type(soup.find_all('img',class_='BDE_Image'))) #<class 'bs4.element.ResultSet'>

print(soup.find_all('img',class_='BDE_Image'))
print(len(soup.find_all('img',class_='BDE_Image')))
for i in soup.find_all('img',class_='BDE_Image'):
    #print(i)
    #print(type(i)) #<class 'bs4.element.Tag'>
    print(i['src'])
    with open('/Users/user/Documents/0015/'+os.path.split(i['src'])[1],'wb') as f: #'/Users/user/Documents/0015/' 需要带最好一个"/" 不然路径拼接会有问题
        f.write(requests.get(i['src']).content)








#利用第三方 requests库实现
# import requests
# from bs4 import BeautifulSoup
#
# url='http://tieba.baidu.com/p/2166231880'
# resp= requests.get(url)
# soup=BeautifulSoup(resp.text,'lxml')
# print(type(soup.find_all('img',class_='BDE_Image'))) #<class 'bs4.element.ResultSet'>
#
# print(soup.find_all('img',class_='BDE_Image'))
# print(len(soup.find_all('img',class_='BDE_Image')))
# for i in soup.find_all('img',class_='BDE_Image'):
#     print(i['src'])
#     with open('/Users/user/Documents/0015/'+os.path.split(i['src'])[1],'wb') as f: #'/Users/user/Documents/0015/' 需要带最好一个"/" 不然路径拼接会有问题
#         f.write(requests.get(i['src']).content)




import urllib.request
from bs4 import BeautifulSoup
import re
import os

url='http://tieba.baidu.com/p/2166231880'
content=urllib.request.urlopen(url).read().decode()
soup=BeautifulSoup(content,'lxml')  #将待解析的content（html格式），按照'lxml'解释器进行解析
img_list=soup.find_all('img',class_='BDE_Image')  #查找的时候  最好直接找最里层的内容（soup.find_all（）方法只要是tag即'<' 或者<>，都能够被检索，不管是在外城还是内层）
print(len(img_list))
i=0
for img in img_list:
    with open('/Users/user/Documents/0013/'+os.path.split(img['src'])[1],'wb') as f:
        f.write(urllib.request.urlopen(img['src']).read())

     #urllib.request.urlretrieve(img['src'], '/Users/user/Documents/0014/'+os.path.split(img['src'])[1])


# import requests
# import ssl
# ssl._create_default_https_context=ssl._create_unverified_context
# request = requests.get('https://api.github.com/events')
# print('request.text', request.text)
# print('request.json()', request.json())

