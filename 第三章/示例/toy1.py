#!/usr/bin/env python3
# coding=utf-8

"""字符串格式化

    使用 format % values 可以对字符串进行格式化
    语法类似C语言里的printf。values可以是单个字符串，
    int类型或则其他对象，也可以是元组字典等。
"""

fmt1 = 'Hi %s!'
fmt2 = 'Hi %s, your user id is %s!'
user = 'urain39'
user_id = 1000

# 格式化单个变量
s1 = fmt1 % user              # R => "Hi urain39!"

# 格式化多个变量
s2 = fmt2 % (user, user_id)   # R => "Hi urain39. your user id is 1000!"

print(s1 + '\n' + s2)

