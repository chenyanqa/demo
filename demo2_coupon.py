#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200
个激活码（或者优惠券）

参考：https://www.cnblogs.com/gongxr/p/7257864.html
print(random.random()) #返回一个0-1之间的任意小数
print(random.randint(1,10)) #返回一个1-10之间的任意整数

for i in range(5):
	print(random.randrange(0,21,1)) # 这里的“1 ”为步长

list =['string',2,'a','123']
print(random.choice(list)) #返回一个字符
print(random.choices(list)) #返回一个list

random.shuffle(list) #将list 里面的元素随机打乱，该函数本身返回null
print(list)

print(random.sample(list,2)) #从list里面任意截取一个长度为2的list
'''

#test
# import random
# list1 = list()
# for i in range(200):
# 	a = random.randint(0,1000)
# 	list1.append(a)
# print(list1)


#方法1：使用uuid模块，uuid1基于MAC地址，时间戳，随机数来生成唯一的uuid，可以保证全球范围内的唯一性。
import string
import uuid
# result=list()
# for i in range(20):
# 	uuid_1 = uuid.uuid1()
# 	uuid_temp = str(uuid_1).replace('-', '')
# 	uuid_2 = uuid_temp[0:15]
#
# 	if uuid_2 not in result:
# 		result.append(uuid_2)
# 	else:
# 		continue
#
# print(result)


# def create_num(count,length):
# 	#result=list() 都表示创建一个空list
# 	result=[]
# 	for i in range(count):
# 		uuid_1 = uuid.uuid1()
# 		uuid_temp = str(uuid_1).replace('-', '')
# 		uuid_2 = uuid_temp[0:length]
#
# 		if uuid_2 not in result:
# 			result.append(uuid_2)
# 		else:
# 			continue
# 	return result
#
# if __name__=='__main__':
# 	for i in create_num(20,15):
# 		print(i)


#方法2：使用random.choice()方法
import random
import string
# str1=string.ascii_letters+'0123456789'
# result=[]
# for i in range(20):
# 	list1 = []
# 	for j in range(15):
# 		list1.append((random.choice(str1)))
#
# 	result.append(''.join(list1))
#
# print(result)
#

def create_num(count,length):
	str1 = string.ascii_letters+'0123456789'

	result= []
	for i in range(count):
		list1=[]
		for j in range(length):
			list1.append(random.choice(str1))

		result.append(''.join(list1))
	return result

if __name__=='__main__':
	for i in create_num(20,15):
		print(i)

