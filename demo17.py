#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
知识点：
1、这是因为json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False：
2、python3 之前一般默认的编码格式时 ascii  无法正常解析中文，但是utf-8编码支持中文解析，所以需要先申明
编码方式，python3之后 默认的编码方式为utf-8 了





'''

'''
https://www.cnblogs.com/liez/p/5406621.html
https://blog.csdn.net/huangxiongbiao/article/details/45974247
https://www.cnblogs.com/fnng/p/3581433.html

将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如

下所示：

<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!--
	学生信息表
	"id" : [名字, 数学, 语文, 英文]
-->
{
	"1" : ["张三", 150, 120, 100],
	"2" : ["李四", 90, 99, 95],
	"3" : ["王五", 60, 66, 68]
}
</students>
</root>


dict1={}
dict1['name']='chenyan'
dict1['age']=20
print(dict1) #print(worksheet.nrows)

'''

import xlrd
import json
import xml.dom.minidom as md

import xml.etree.cElementTree


workbook=xlrd.open_workbook('student1.xls')
worksheet=workbook.sheet_by_index(0)

'''
print(worksheet.row(0))
print(worksheet.row_values(0))
print(worksheet.nrows)

'''
contents={}

for i in range(worksheet.nrows):
    contents[i+1]=worksheet.row_values(i)[1:]

print(contents)

'''
是自动补全的变量的类别
p：parameter 参数
m：method 方法
c：class 类
v：variable 变量
f：function 函数
'''
xml_s=md.Document() #创建一个xml.dom.minidom.Document 对象
root=xml_s.createElement('root')
students=xml_s.createElement('students')

xml_s.appendChild(root)
root.appendChild(students)

#comment=xml_s.createComment('<!--学生信息表 "id" : [名字, 数学, 语文, 英文]-->')
comment=xml_s.createComment('学生信息表 "id" : [名字, 数学, 语文, 英文]')

students.appendChild(comment)

text=xml_s.createTextNode(json.dumps(contents,ensure_ascii=False))
students.appendChild(text)

#将xml.dom.minidom.Document 对象的内容写入到.xml文件中


with open('students1.xml','wb') as f:
    f.write(xml_s.toprettyxml(encoding='utf-8'))  #这里加了encoding 属性后，就需要将xml文件的打开模式变为'wb'写入

















# import xlrd
# import json
# import xml.dom.minidom as md
#
# #通过打开已有excel文件穿件新的excel文件对象及对应的sheet表
# workbook= xlrd.open_workbook('student1.xls')
# worksheet= workbook.sheet_by_index(0)  #将student1.xls的表格 按照索引位置来生成一个新的表格，返回一个xlrd.sheet.Sheet对象
# #worksheet=workbook.sheet_by_name('student') #按照名字来生成新的表格，前提是打开的表格有固定的命名
# # print(workbook.sheet_names()) #['student']
# # print(workbook.sheets()) #[<xlrd.sheet.Sheet object at 0x1018d95c0>]
# # print(worksheet.nrows) #3
#
#
#
# # 读取打开的excel sheet表的内容，并转成dict
# # content={}
# # for i in range(worksheet.nrows):
# #     content[i+1]=worksheet.row_values(i)[1:]
# #
# # print(content)
#
# content={}
# for i in range(worksheet.nrows):
#     list=worksheet.row_values(i)
#     content[list[0]]=list[1:]
#
# print(json.dumps(content,ensure_ascii=False))
#
#
# #通过xml.dom.minidom 库创建xml
#
# xmlfile=md.Document()  #创建xml文件
# print(xmlfile)
#
# root = xmlfile.createElement('root') #创建 根节点
# students=xmlfile.createElement('students') #创建students节点
#
# xmlfile.appendChild(root) #在文件下添加root节点
# root.appendChild(students) #在root节点下添加students节点
#
# comment=xmlfile.createComment('学生信息表 "id" : [名字, 数学, 语文, 英文]')  #创建评论
# students.appendChild(comment)  #在students 节点下添加评论
#
# xmlcontent=xmlfile.createTextNode(json.dumps(content,ensure_ascii=False)) #创建文本节点
# students.appendChild(xmlcontent)  #在students标签下添加文本内容
#
# print(xmlfile.toprettyxml())
#
# # with open('students.xml','wb') as f:
# #     #f.write(xmlfile.toprettyxml(encoding='utf-8')) #写入文件 以比较规范的格式
# #     f.write(xmlfile.toxml(encoding='utf-8')) #写入文件，以普通的xml格式（所以内容一行展示）








