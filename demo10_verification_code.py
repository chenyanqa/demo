#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
使用 Python 生成类似于下图中的字母验证码图片
'''

import random
import string

from PIL import Image



list1 = []
string1 = string.ascii_uppercase
for i in range(4):
    list1.append(random.choice(string1))

print(list1)

newimg= Image.new("RGBA",(500,100),(255,0,0))
newimg.show()


