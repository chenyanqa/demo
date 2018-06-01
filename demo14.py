#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''

 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中，如下图所示：

'''

import csv
import json
list=[]
with open('/Users/user/Documents/student.txt','rb') as f:
    #print(type(f.read().decode())) #<class 'str'>
    #print(type(json.loads(f.read().decode()))) #<class 'dict'>
    #print(json.loads(f.read().decode()))
    # dict=json.loads(f.read().decode())
    # print(list)

    # #print(f.readlines())
    # for line in f.readlines():
    #     #print(line.decode().strip())
    #     list.append(line.decode().strip())
    dict = json.loads(f.read().decode())
    print(dict)

    for i in dict:
        list.append(i.keys)
        list.append(i['value'])


print(list)


# with open('/Users/user/Documents/student.csv','wb') as f:
#     f_csv=csv.writer(f)
#     f_csv.write
#

