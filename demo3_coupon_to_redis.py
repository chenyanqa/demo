#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
**将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
'''

import random
import string
import redis


str1 = string.ascii_letters+string.digits

def create_coupon(count,length):
	result=[]
	for i in range(count):
		list1=[]
		for j in range(length):
			list1.append(random.choice(str1))

		if ''.join(list1) not in result:
			result.append(''.join(list1))
		else:
			continue
	return result

#1、将数据以set（无序且唯一的集合）存储在redis中
def save_to_redis(codes):
	r = redis.Redis(host='127.0.0.1',port=6379)
	for i in codes:
		r.sadd("code",i)  #在控制台使用smembers code
	r.save()

	print(r.smembers("code")) #读取所有数据

	for i in r.smembers("code"): #由于redis 里面读取出来的数据都是byte比特流数据，因此需要通过decode（）方法解码为字符串
		print (i.decode())

#2、将数据以list的形式存储在redis中
# def save_to_redis(codes):
# 	r = redis.Redis(host='127.0.0.1',port=6379,db=1)
# 	for i in codes:
# 		r.rpush("code",i)  #在控制台使用 127.0.0.1:6379[1]> lrange code 0 -1 读取数据
# 	r.save()
#
# 	print(r.lrange("code",0,-1))


if __name__=='__main__':
	save_to_redis(create_coupon(20,15))

# import redis
# '''
# 127.0.0.1:6379[1]> rpush 0 88 99 100
# (integer) 9
# 127.0.0.1:6379[1]> lrange 0 0 -1
# 1) "11"
# 2) "4"
# 3) "3"
# 4) "2"
# 5) "1"
# 6) "77"
# 7) "88"
# 8) "99"
# 9) "100"
# '''
# r = redis.Redis(host='127.0.0.1', port='6379', db=1,decode_responses=True)
# r.lpush("0",1,2,3,4)  #表示向key 为0，插入值为“1”，“2”。。
# print(r.lrange("0", 0, -1))