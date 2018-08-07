#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}

请将上述内容写到 city.xls 文件中，如下图所示： city.xls


1、rb+ 模式读取：[b'{\n', b'    "1" : "\xe4\xb8\x8a\xe6\xb5\xb7",\n', b'    "2" : "\xe5\x8c\x97\xe4\xba\xac",\n', b'    "3" : "\xe6\x88\x90\xe9\x83\xbd"\n', b'}']
2、r+ 模式读取：['{\n', '    "1" : "上海",\n', '    "2" : "北京",\n', '    "3" : "成都"\n', '}']
总结：rb 表示以二进制方式读取，最好用于读取二进制文件，而r 表示以普通文本方式读取，最好用于读取文本文件


3，file.read() 返回一个str  file.readlines() 返回一个list

'''


import json
import xlwt


#读取txt里面内容并保持为字典格式
with open('/Users/user/Documents/demo/city.txt','r+') as f:
    data=json.loads(f.read()) #将str（unicode） 反解析为python对象
    #data=json.load(f)   #从文件中将str反解析为python对象

    print(type(data)) #<class 'dict'>
    print(data)  #{'1': '上海', '2': '北京', '3': '成都'}
    print(data.items()) #dict_items([('1', '上海'), ('2', '北京'), ('3', '成都')])
    print(enumerate(data.items()))

#创建excel文件及excel sheet页
workbook=xlwt.Workbook(encoding='ascii')
worksheet=workbook.add_sheet('city')


#往excel中写入文件
# enumerate(object) ->  (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
'''
Traceback (most recent call last):
  File "/Users/user/Documents/demo/demo15.py", line 48, in <module>
    for index,k,v in enumerate(data.items()):
ValueError: not enough values to unpack (expected 3, got 2)


==>for index,(k,v) in enumerate(data.items())

'''
for index,(k,v) in enumerate(data.items()):
    i=0 #表示列
    worksheet.write(index,i,k)
    worksheet.write(index,i+1,v)

workbook.save('/Users/user/Documents/demo/city.xls')











