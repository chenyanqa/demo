#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
1)  PIL 库 The Python Imaging Library.

'''
from PIL import Image,ImageDraw
import os

#
# file = open(r'D:\cy\ddemo\photos','rw')
# file.read()

#print(os.walk('D:\cy\ddemo\photos'))

for root, dirs, files in os.walk('D:\cy\ddemo\photos'):
	print(root) #当前目录路径
	print(dirs) #当前路径下所有子目录
	print(files) #当前路径下所有非目录子文件
