#!/usr/bin/env python
# -*- coding:utf-8 -*-

#题目：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果

from PIL import Image,ImageDraw,ImageFont

# #方法1：
# img = Image.open(r"D:\cy\ demo\demo1.jpg",'r').convert('RGB') #这里windows 上如果不加.convert()方法的话，save图片会报错
# draw = ImageDraw.Draw(img)  #生产一个画图ImageDraw
# #print(type(draw)) #<class 'PIL.ImageDraw.ImageDraw'>
#
# myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=30)
# fillcolor = "#ff0000"
# #print(img.size) #(300, 300)
#
# width,height = img.size
# #text(xy, text, fill=None, font=None, anchor=None, *args, **kwargs)
# draw.text((width-20,0),'4', font=myfont, fill=fillcolor)
#
# #img.show()
# #save(fp, format=None, **params) fp表示讲文件保存的路径，后面的format 表示格式，若前面路径中已经指定图片格式了，则后面的格式不会生效
# img.save('result1.jpeg','png')


#方法2：通过函数 (注意函数名或者类名可以跟python文件名相同)
# def add_num(img):
# 	draw=ImageDraw.Draw(img)
# 	myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf',size=30)
# 	fillcolor = "#ff0000"
# 	width,height=img.size
# 	draw.text((width-20,0),'4',fill=fillcolor,font=myfont)
# 	img.show()
# 	img.save('result2.png','png')
# 	#return 0
#
# if __name__=='__main__':
# 	image=Image.open(r"D:\cy\ demo\demo1.jpg",'r').convert('RGB')
# 	add_num(image)
#

