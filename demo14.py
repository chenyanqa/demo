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

参考：https://blog.csdn.net/destinymf/article/details/78096678
https://blog.csdn.net/joey_2018_/article/details/80653671
https://blog.csdn.net/wangran51/article/details/8512682
https://github.com/Show-Me-the-Code/python/blob/master/monkey/0014/main.py


'''

import csv
import json
# list=[]
# with open('/Users/user/Documents/student.txt','rb') as f:
#     #print(type(f.read().decode())) #<class 'str'>
#     #print(type(json.loads(f.read().decode()))) #<class 'dict'>
#     #print(json.loads(f.read().decode()))
#     # dict=json.loads(f.read().decode())
#     # print(list)
#
#     # #print(f.readlines())
#     # for line in f.readlines():
#     #     #print(line.decode().strip())
#     #     list.append(line.decode().strip())
#     dict = json.loads(f.read().decode())
#     print(dict)
#
#     for i in dict:
#         list.append(i.keys)
#         list.append(i['value'])
#
#
# print(list)



import xlrd,xlwt,json

'''
1,dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
        Serialize ``obj`` to a JSON formatted ``str``.
        把对象转换为字节序列的过程成为对象的序列化（保存文件、网络上传输数据都需要将数据先序列化，python中str默认使用
        unicode编码）

2,loads(s, *, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
        Deserialize ``s`` (a ``str``, ``bytes`` or ``bytearray`` instance
        containing a JSON document) to a Python object.
        把字节序列恢复为对象的过程称为对象的反序列化。

3，dumps是将dict转化成str格式，loads是将str转化成dict格式。
dump和load也是类似的功能，只是与文件操作结合起来了

4, file=open('/Users/user/Documents/demo/student.txt','r+')
   lines= file.readlines() #将每行内容包含换行，空格等 都保存成一个list

['{\n', '\t"1":["张三",150,120,100],\n', '\t"2":["李四",90,99,95],\n', '\t"3":["王五",60,66,68]\n', '}']

5、students = [('kohn', 'A', 15), ('eane', 'B', 12), ('dave', 'C', 18)]
print(sorted(students,key=lambda s:s[2])) #表示讲students 按照每个元祖的索引位置为2的元素进行排序

6、先看lambda函数是什么意思？
>>> f=lambda x:x+1
>>> f(2)
3
很简单了，x是参数，x+1是函数返回值。

'''

#创建excel文件及excel sheet页
workbook=xlwt.Workbook(encoding='utf-8')
worksheet=workbook.add_sheet('student')


#将.txt 文件中的json串 反解析为python对象并保存在变量data中
with open('/Users/user/Documents/demo/student.txt','r+') as f:
    print(type(f)) #<class '_io.TextIOWrapper'>  json
    #data = json.loads(f) 这个会报错，因为json.loads()的操作对象必需是str类似，文件类型的 需要用json.load()
    data=json.load(f)

#print(type(data)) #<class 'dict'> 将str类似数据转成python对象
#print(data)  #{'1': ['张三', 150, 120, 100], '2': ['李四', 90, 99, 95], '3': ['王五', 60, 66, 68]}

# print(data.items())
# print(sorted(data.items(),key=lambda d:d[1]))
# print(data.values())
# print(data.keys())
'''
dict_items([('1', ['张三', 150, 120, 100]), ('2', ['李四', 90, 99, 95]), ('3', ['王五', 60, 66, 68])])
dict_values([['张三', 150, 120, 100], ['李四', 90, 99, 95], ['王五', 60, 66, 68]])
dict_keys(['1', '2', '3'])

product = ["Mac pro", "iPhone", "iWatch"]
for index, item in enumerate(product):
    print(index, item)
'''
#方法1：
# for index,(key,values) in enumerate(data.items()):
#     worksheet.write(index,0,key)
#     for i,value in enumerate(values):
#         worksheet.write(index,i+1,value)  # sheet1.write('行号’,'列号'，‘值’)#向excel中写入数据
#
# workbook.save('/Users/user/Documents/demo/student.xls')


#方法2：
row=0
col=0
#sorted(data.items(),key=lambda d:d[0])  #[('1', ['张三', 150, 120, 100]), ('2', ['李四', 90, 99, 95]), ('3', ['王五', 60, 66, 68])]
for key,value in sorted(data.items(),key=lambda d:d[0]): #将data.items() 按照每个元组中的 索引位置为1 的元素进行排序
    worksheet.write(row,col,key)
    for i in value:
        col=col+1
        worksheet.write(row,col,i)

    row=row+1
    col=0

workbook.save('/Users/user/Documents/demo/student1.xls')




# import chardet
# f = open('/Users/user/Documents/demo/student1.csv','rb')
# data=f.read()
# print(data)
# print(chardet.detect(data))




