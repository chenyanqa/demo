#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
使用 Python 生成类似于下图中的字母验证码图片
'''

import random
import string
from PIL import Image,ImageDraw,ImageFont

#方法1：生成随机字符，然后生成一张图片，然后在图片上写入随机字符
# list1 = []
# string1 = string.ascii_uppercase
# for i in range(4):
#     list1.append(random.choice(string1))
#
# newimg= Image.new("RGB",(400,100),(255,0,0))
# font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf",30)
#
# draw = ImageDraw.Draw(newimg)
# # draw.line((0,0,500,100),fill=128)  #画直线 的坐标 需要在一个元组中 保护起点和终点坐标，其实（0，0）表示左上角
# # draw.line((500,0,0,100),fill=128)
#
# for i in range(4):
#     draw.text((80*(i+1),35),list1[i],font=font,fill=109)
#
# newimg.show()


#方法2：使用函数的方法

def randChar():
    #return chr(random.randint(65,90))
    return random.choice(string.ascii_uppercase) #返回 N
    #return random.choices(string.ascii_uppercase)  #返回 ['N']

def randColor():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def createVerificationCode(size,charnum):
    width=size*charnum
    height=size

    img=Image.new("RGB",(width,height),(255,255,255))
    print(img.mode) #RGB
    print(img.getbands())  # RGB
    draw=ImageDraw.Draw(img)

    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=randColor())

    font=ImageFont.truetype("C:\Windows\Fonts\Arial.ttf",size)
    #print(draw.textsize('AH'))

    for i in range(charnum): #draw.text()中的（x，y）表示距离左上角的距离，但是由于文字本身填充，所有及时为（0，0）也会不完全是在左上角
        draw.text((size*i+10,-5),text=randChar(),font=font,fill=randColor())
        print(draw.textsize('G'))

    img.show()
    img.save('verification_code.jpg') #save(self, fp, format=None, **params)


if __name__=='__main__':
    createVerificationCode(60,4)

# img1=Image.open('verification_code.jpg')
# print(img1.format) #JPEG