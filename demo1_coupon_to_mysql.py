#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
1、刚开始使用pymysql链接数据库的时候 总是报错1045，ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
解决办法：更新了一下 root的密码 ：
use mysql；
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '你的密码';
FLUSH PRIVILEGES;

2、conn.commit()\close()等操作  最好等数据批量操作完以后再提交\关闭

3 创建数据库代码: (id 主键 自增)
	cursor.execute("create table coupon_code(id int auto_increment PRIMARY key,couponcode VARCHAR(30))")

4 往数据库插入数据,且值从变量中取值:
	for i in codes:
		cursor.execute("insert into coupon_code(couponcode) VALUES(%s)",(i)) #这里的i 每次从codes中取,自增的id 如果不插入值的
		话,mysql会自动处理

'''

import random
import string
import pymysql

# str1 = string.ascii_letters + '0123456789'
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

#1、直接在mysql中先创建数据库及表
# def save_couponcode(codes):
# 	conn = pymysql.connect(host="localhost",port=3306,user="root",passwd='chen123',db="test",charset='utf8')
# 	cursor=conn.cursor()
#
# 	for i in codes:
# 		cursor.execute('insert into coupon(couponcode) VALUES (%s)',i)
# 		conn.commit()
#
# 	conn.close() #数据库连接结束 要在所有sql执行完毕以后，不然容易报错pymysql.err.InterfaceError: (0, '')
#
# if __name__=='__main__':
# 	save_couponcode(create_coupon(20, 15))

#2、从代码中创建数据库及表
def save_codes(codes):
	conn = pymysql.connect(host="localhost",port=3306,user="root",passwd="chen123",db="test")
	cursor=conn.cursor()

	cursor.execute("drop table if EXISTS coupon_code")
	cursor.execute("create table coupon_code(id int auto_increment PRIMARY key,couponcode VARCHAR(30))")

	for i in codes:
		cursor.execute("insert into coupon_code(couponcode) VALUES(%s)",(i))

	conn.commit() #循环插入执行完后 在统一提交
	cursor.close()
	conn.close()

if __name__=='__main__':
	save_codes(create_coupon(20, 15))
