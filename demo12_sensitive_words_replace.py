#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
 1）在for循环完整完成后才执行else；如果中途从break跳出，则连else一起跳出。
'''

def replace_sensitive_words():
	words = []
	with open('sensitive_words.txt', 'r+') as f:
		for line in f.readlines():
			words.append(line.strip())

	iw = input('enter your words: ')
	for i in range(len(words)):
		if iw.find(words[i]) > -1: #str.find('str1') 如果找不到 则返回-1
			iw=iw.replace(words[i],'*'*len(words[i])) #iw.replace(old,new) 会返回替换后的字符串，但是iw不会被改变
			continue

	else:
		print('Human Rights')

	return iw

if __name__=='__main__':
	print(replace_sensitive_words())



# words = []
# with open('sensitive_words.txt', 'r+') as f:
# 	for line in f.readlines():
# 		words.append(line.strip())
#
# print(words) #['北京', '程序员', '公务员', '领导', '牛比', '牛逼', '你娘', '你妈', 'love', 'sex', 'jiangge']
# iw = input('enter your words: ')
# print(iw.find('公务员'))
#
# for i in range(len(words)):
# 	if iw.find(words[i]) > -1:
# 		print('Freedom')
# 		break
# else:
# 	print('Human Rights')


# str1 = "this is string example....wow!!!";
# str2 = "str";
# print(str1.find(str2))
# print(str1.replace('this','*'*2))
# print(str1)