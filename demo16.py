#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

[
	[1, 82, 65535],
	[20, 90, 13],
	[26, 809, 1024]
]
'''



import json
import xlwt


#读取文件
with open('/Users/user/Documents/demo/numbers.txt','r+') as f:
    data=json.load(f)
    print(data)


#创建excel文件及sheet页
workbook=xlwt.Workbook(encoding='ascii')
worksheet=workbook.add_sheet('numbers')

#写入文件
for index,seq in enumerate(data):

    for index1,s in enumerate(seq):
        worksheet.write(index,index1,s)

workbook.save('/Users/user/Documents/demo/numbers.xls')

