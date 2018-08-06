#!/usr/bin/env python3
# coding=utf-8

"""字符串的替换


    # 匿名字段替换（没有名字的字段） #
    "{}你好!"，其中的“{}”就是匿名字段
    可以使用"{}你好".format("urain39")方法对其进行格式化
    多个“{}”会自动按顺序替换，不能与下面的索引替换混用！
    
    
    # 索引字段替换 #
    在“{}”中填上索引序号如"{1}{2}{0}"就能不按照顺序替换


    # 命名字段替换 #
    在“{}”中填入一个标识符，如“{name}”称为命名替换
    使用“{name}”.format(name="urain39")来替换，其中name为关键字参数
    
    使用“{标识符:格式化符}”可以对替换就行格式化，如：
    "{pi:.2f}".format(pi=3.141592) => '3.14'


    # 模板字符串 #
    类似Unix Shell语法，使用$标识的替换i
    你也可以写成${标识}的格式，与上面等同
    使用substitute()方法进行替换，传入关键字参数即可

"""


# 匿名字段
s_tmp = "{}你好！"
print(s_tmp.format("urain39"))                              # => "urain3i你好"


# 索引字段
print("{1} {3} {2} {0}".format("back", "I", "be", "will"))  # => "I will be back"


# 命名字段
print("Hello {name}".format(name="urain39"))                # => "Hello urain39"
print('pi = {pi:0.2f}'.format(pi=3.141592))                 # => 'pi = 3.14'


# 模板字符串
import string

tmpl = string.Template("${lang} is the best one")
print(tmpl.substitute(lang='Python'))                       # => "Pyhon is the best one"


