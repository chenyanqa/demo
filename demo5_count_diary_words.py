#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
1、方法1 ：先通过os.listdir(path)等 列举出当期目录中的文件，然后遍历每个文件，读取文件中的内容，将一些空格，逗号，点号等都变成空格
（用replace(str，str)方法）然后 通过split（）方法 将内容按照空格分割为单个单词组成的list，然后使用collections的Counter（）方法
统计list的单词出现频率并排序，最后通过Counter的most_common(1)方法获取出现频率最高的一项

2、统计出现频率相关的 应该首先考虑用collections模块，比较方便

3、分词等可以考虑使用正则，例如将包含英文字母组成的单词摘出来，re.findall(r'[A-Za-z]+',text.lower())
4、os.listdir(path)   列举当前目录的文件，包含因此文件，os.path.join(path,1.txt) 将path 和"1.txt" 拼接为一个完整的路径
os.path.basename(filepath) 此时filepath 为一个完整的路径，取其文件名 ，即1.txt等

'''

import os
import collections


# #方法1：
# path='/Users/user/Documents/demo/diary/'
# files=os.listdir(path)
#
#
# for f in files:
#     if f.startswith('.'):
#         files.remove(f)
#
# print(files)
#
# for f in files:
#     abspath=path+f
#     with open(abspath,'rb+') as f1:
#         txt = f1.read().decode()
#         txt_new = txt.replace(',', ' ').replace('.', ' ').replace('--', ' ').replace('"', ' ') #最好还是用正则表达式分词
#         words = txt.strip().split(' ')
#         print(words)
#         c_list=collections.Counter(words).most_common(1) #通过.most_common()方法将dict转为list
#         #print(c_list) #[('s', 4)] ,然后c_list[0] 表示把第一个元组取出来，然后c_list[0][0] 表示取出元组的第一个元素
#         print('日记%s 出现频率最高的词为%s，出现次数为：%s'%(f,c_list[0][0],c_list[0][1]))
#


#方法2：
import os
import re
import collections


def get_filepath(path):
    filepath=[]
    files=os.listdir(path)
    for f in files:
        if f.endswith('.txt'):
            filepath.append(os.path.join(path,f))

    return filepath


def get_words(filepath):
    with open(filepath,'rb+') as f:
        text=f.read().decode()
        words_list=re.findall(r'[A-Za-z]+',text.lower())
        print(words_list)
        c=collections.Counter(words_list).most_common(1)
        print('文件%s,出现频率最高的词是%s，出现次数为：%s'%(os.path.basename(filepath),c[0][0],c[0][1]))


if __name__ == "__main__":
    path = '/Users/user/Documents/demo/diary/'
    for file in get_filepath(path):
        get_words(file)



