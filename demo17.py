#!/usr/bin/env python3
# -*- coding:utf-8 -*-

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

'''


import xlrd
import xml.dom.minidom as md


workbook= xlrd.open_workbook('student1.xls')
#worksheet= workbook.sheet_by_index(0)
worksheet=workbook.sheet_by_name('student')

