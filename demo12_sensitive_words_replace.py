#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
 1）在for循环完整完成后才执行else；如果中途从break跳出，则连else一起跳出。
 2）while-true中 一定要有break语句，否则会造成死循环
 3）该py文件 在windowns下编码是正常的，但是转到mac上后，编码一直报错，例如
 with open('sensitive_words.txt', 'r', encoding='utf8') as f
 UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb1 in position 0: invalid start byte

 然后经过排查发现，文件sensitive_words.txt 在mac下打开是乱码，发现其编码使用的是：ISO-8859-1
由于该文件是中文，因为选择编码为gb2312 后，该文件内容中的文案展示正常，然后在该文件的 open（）方法中 ，添加encodeing='gb2312'
即可。

4）由于unicode是万国码，兼容性强 因此绝大部分应用和系统内部都是使用unicode作为程序内码的，所以其他编码方式的字符要被
python理解，需要先解码为unicode，然后pyhton 解释器在将unicode字符 编译成其他编码 交给cpu操作

例如 打开某个网页，由于网页上传输的内容 都是通过bytes比特流的形式传输的，因此 直接read（）后，是b"。。。"的形式，因此
需要使用decode（）方法 将bytes字符转换为str-unicode的形式，且python中默认 可见的字符str，程序代码等 都是unicode编码

'''

def replace_sensitive_words():
    words = []
    with open('sensitive_words.txt', 'r', encoding='gb2312') as f:#表示带打开的文件默认是gb2312的形式编码的，你需要通过gb2312的形式去解码为unicode
        for line in f.readlines():
            words.append(line.strip())

    iw = input('enter your words: ')
    flag = 0  # 用于标识是否找到敏感词，找到则置为1

    for i in range(len(words)):
        if iw.find(words[i]) > -1:  # str.find('str1') 如果找不到 则返回-1
            flag = 1
            iw = iw.replace(words[i], '*' * len(words[i]))  # iw.replace(old,new) 会返回替换后的字符串，但是iw不会被改变
            continue

    if flag == 0:
        print('没有敏感词，human right')
    else:
        return iw


if __name__ == '__main__':
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


# words = []
# with open('sensitive_words.txt', 'r') as f:
# 	# for line in f.readlines():
# 	# 	words.append(line.strip())
# 	print(f.read())
#
#
# #print(words)
#
#
# import chardet
# chardet.detect(b'\xb1\xb1\xbe\xa9')
# #{'encoding': 'ISO-8859-1', 'confidence': 0.73, 'language': ''}



# #while-true用法：
#
# list_words = ['北京', '程序员', '公务员', '领导', '牛比', '牛逼', '你娘', '你妈', 'love', 'sex', 'jiangge']
#
# while True:
#     input_word = input('请输入：')
#
#     for i in range(len(list_words)):
#         if input_word.find(list_words[i]) > -1:
#             input_word = input_word.replace(list_words[i], '*' * len(list_words[i]))
#
#     else:
#         print(input_word)
#         break
