#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
1)那么str.strip()就是把这个字符串头和尾的空格，以及位于头尾的\n \t之类给删掉。
2)f.read()返回一个字符串，f.readlines()返回一个list
'''

# 简单思路：
# f = open('sensitive_words.txt','r+')
# #print(f.read())
#
# word= input('请输入：')
#
# if word in f.read():
# 	print('Freedom')
# else:
# 	print('Human Rights')


#方法1：使用f.read()方法 一次性读取全部内容，然后再跟用户的输入作比较
# def test_input(word,f):
# 	if word in f.read():
# 		print('Freedom')
# 	else:
# 		print('Human Rights')
#
# if __name__=='__main__':
# 	f= open('sensitive_words.txt','r+')
# 	word = input('请输入：')
# 	test_input(word,f)


#方法2：使用f.readlines()先把结果放到一个列表中，然后再去判断用户的输入
def filterwords():
    words = []
    with open('sensitive_words.txt', 'r+') as f:
        for line in f.readlines():
            words.append(line.strip())

    iw = input('enter your words: ')
    for i in range(len(words)):  #for 如果正常执行完，则会执行else，若for是break中断的，则会连else也一起中断
        if iw.find(words[i]) >-1:
            print('Freedom')
            break
    else:
        print('Human Rights')

if __name__ == '__main__':
    filterwords()


# f = open('sensitive_words.txt', 'r+')
# list1=[]
# print(f.read())
# # #print(f.readlines()) #['北京\n', '程序员\n', '公务员\n', '领导\n', '牛比\n', '牛逼\n', '你娘\n', '你妈\n', 'love\n', 'sex\n', 'jiangge']
# # for i in f.readlines():
# # 	list1.append(i.strip())
# # print(list1)