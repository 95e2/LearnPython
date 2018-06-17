第五章
===============



#### 朝花夕拾 ####

> 不知道这个名字是否有点过了，但这一章开头确实是回顾性的来介绍print与import语句的其他用处，所以我认为“朝花夕拾”这个名字可能比较适合作为这一段的小标题。



##### 连接字符串

```python
# 使用'+'连接字符串后使用print输出
print('Hello' + ', World!') # => Hello, World!
```

##### print函数自定义结尾符号 #####

```python
# print函数在打印输出时默认会输出后换行
print('Hello, World!')         # => Hello, World!<newline>

# 如果我们像去掉这个换行符，我们可以使用
# 关键字参数end=''来解决这个问题，如下所示
print('Hello, World!', end='') # => Hello, World!
```

书中还有一个介绍如何使用sep关键字的一段，但是我认为sep参数与前面的str.join方法有点类似，故不作详细介绍。下面引用了Python3文档中关于print的一部分，可以作为参考。

##### print函数的其他关键字参数及其描述 #####

> Help on built-in function print in module builtins:
>
> print(...)
>     print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
>     
>     Prints the values to a stream, or to sys.stdout by default.
>     Optional keyword arguments:
>     file:  a file-like object (stream); defaults to the current sys.stdout.
>     sep:   string inserted between values, default a space.
>     end:   string appended after the last value, default a newline.
>     flush: whether to forcibly flush the stream.



##### import解决模块重名问题 #####

```python
# 当我们试图从其他模块中导入函数时，通常我们会遇到多个函数重名的情况
# 假设我们的MyApp模块中有一个名为open的函数，使用如下命令
from myapp import open
# 导入将会覆盖掉当前环境下的open函数，对此我们应使用如下语法解决
from myapp import open as my_open
```



#### 序列解包 ####

> 赋值语句你见过很多，有的给变量赋值，还有的给数据结构的一部分（如列表中的元素和切 片，或者字典项）赋值，但还有其他类型的赋值语句。例如，可同时（并行）给多个变量赋值的序列解包（或可迭代对象解包）：将一个序列（或任何可迭代 对象）解包，并将得到的值存储到一系列变量中。

##### 小试牛刀 #####

```python
values = 1, 2, 3
values = (1, 2, 3)

print(values) # => (1, 2, 3)

# 上面的代码其实与下面的代码是等价的
# 在Python中多个右值以逗号分隔通常被理解为元组
# 这一点我忘了书里有没有写明了，翻看了之前的笔记这一点是没找到的

# 我们可以定义一个函数来返回两个返回值来验证这一观点
# 比如dict.popitem()方法就能够返回以一个键值对

d = {'a': 1, 'b': 2, 'c', 3}
kv = d.popitem() # 获取键值，并赋值给kv
print(kv) # => '('c', 3)'

k, v = d.popitem() # 获取键值，并分别赋值给k和v
print(k) # => 'b'
print(v) # => 2
```

##### 大显身手(误) #####

```python
def get_next_point(x, y):
    return x + 1, y + 1

get_next_point(1, 3) # -> (2, 4)

x, y = get_next_point(1, 3)
print(x) # => 2
print(y) # => 4
```

因为篇幅问题这里不在多做解释，使用过程中可以自行领会。

##### 收集多余的值 #####

```python
# 假设我们有一长串的数字，但是我们暂时只需要首尾的数值
# 那么这时候我们就可以用到星号来收集中间多余的数值

first, *middle, last = 0, 1, 2, 3, 4, 5, 6, 7

print(first)  # => 0
print(last)   # => 7
print(middle) # => [2, 3, 4, 5, 6]

# 甚至在我们赋值只有两个元素的序列时这条语句仍然是有效的
first, *middle, last = 0, 1

print(first)  # => 0
print(last)   # => 1
print(middle) # => []
```

##### 增强赋值 #####

可以不编写代码x = x + 1，而将右边表达式中的运算符（这里是+）移到赋值运算符（=）的前面，从而写成x += 1。 增强赋值，适用于所有标准运算符，如*、/、%等 

```python
i = 1  # -> 1
i += 1 # -> 2
i *= 3 # -> 6
i -= 1 # -> 5
```



> 时间原因，暂时写到这里。书本第69页，pdf 88页。