#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
**任一个英文的纯文本文件，统计其中的单词出现的个数。
https://www.cnblogs.com/wxshi/p/6827056.html
https://blog.csdn.net/qq_32070219/article/details/73381335

'''
# 方法1：现将文章中的 点号、逗号等都替换为空格，然后拿空格分割整个字符串为list
# import collections
# f = open('aticles.txt','r')
#
# data = f.read().strip().replace('. ',' ').replace(', ',' ').replace('.','')
# data1=data.split(' ')
# print(data1)
# print(len(data1))
#
# # for word in data1:
# # 	print(('%s:%s')%(word,data1.count(word))) #这个遍历的时候  会有重复，例如Every出现了多次，则会展示多次
#
# print(collections.Counter(data1)) #会将data1中每个单词个数，然后降序排列


#方法2：使用正则表达式
import re
import collections

def num(path):
	with open(path,'r') as file:
		data=file.read()

		word=re.compile('[a-zA-Z0-9]+')
		words=word.findall(data)
		print(len(words))

		return collections.Counter(words)

		# dict={}
		#
		# for x in words:
		# 	if x in dict:
		# 		dict[x]+=1
		# 	else:
		# 		dict[x]=1
		#
		# return dict

if __name__=='__main__':
	print(num('aticles.txt'))

