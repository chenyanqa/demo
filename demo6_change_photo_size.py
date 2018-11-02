#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''

第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
1，列举某文件夹下所有文件及目录的函数 os.listdir()
2、列表中删除元素list.remove(x)---从list中删除值为x 的值 ,list.pop() 从列表队尾剔除一个元素
3，获取文件的绝对路径方法：例如跟路径为 path='/Users/user/Documents/demo/changephotosize/' (如果需要拼接绝对路径时，最好
在path 后面加个斜杠，不然在拼接时绝对路径时，需要有添加斜杠的代码存在)
1）abspath=os.path.join(path,f)  （这里的f 为文件名os.listdir(path) 所得）
2) abspath=path+f

4、涉及到图片操作时，需要通过引入专门的图片操作库，例如from PIL import Image等，否则不方便直接操作
5，print(os.path.splitext('11.jpg')[0] 获取文件前缀，os.path.splitext('11.jpg')[-1] 获取文件后缀
6、#im.width=iphone5_x  #AttributeError: can't set attribute 图片的尺寸变更只能通过图片的resize（）方法，不能直接赋值变更

'''

import os
from PIL import Image

iphone5_x=1136
iphone5_y=640

path='/Users/user/Documents/demo/changephotosize/'
files = os.listdir(path)
print(files)  #['.DS_Store', '1.jpg', '11.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']

for f in files: #去掉隐藏文件
    if f.startswith('.'):
        files.remove(f)


for f in files:  #从剩余的正常文件中分别打开 获取其图片的长款，跟iphone5的尺寸进行比较，并按照要求剪裁
    abspath=os.path.join(path,f)
    im=Image.open(abspath)
    x,y=im.size #（im.width，im.height），而im.size 是一个元组，元组值不能被改变或者赋值
    print(x,y)

    if x>iphone5_x:
        x_new=iphone5_x
        y_new=int(iphone5_x*y/x) #表示等比例缩放并取整


    if y>iphone5_y:
        y_new = iphone5_y
        x_new = int(iphone5_y*x/y)

        new_im = im.resize((x_new,y_new),Image.ANTIALIAS) # 按照新尺寸对图片进行剪裁，设定ANTIALIAS，即抗锯齿
        new_f = os.path.splitext(f)[0] + '_new' + os.path.splitext(f)[-1] #os.path.splitext(f)[0]，[-1]获取文件前缀，后缀
        new_im.save(path + new_f) #保存剪裁后的图片

print(os.listdir(path))

