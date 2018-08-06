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



#### 链式赋值 ####

**略、**



#### 增强赋值 ####

可以不编写代码x = x + 1，而将右边表达式中的运算符（这里是+）移到赋值运算符（=）的前面，从而写成x += 1。 增强赋值，适用于所有标准运算符，如*、/、%等 

```python
i = 1  # -> 1
i += 1 # -> 2
i *= 3 # -> 6
i -= 1 # -> 5
```



#### 代码缩进 ####

**略、**



#### if语句与if表达式 ####

> 让你能够有条件地执行代码。这意味着如果条件（if和冒号之间的表达式） 为前面定义的真，就执行后续代码块（这里是一条print语句）；如果条件为假，就不执行（你应 该猜到了）。 

##### if语句 #####

**略、**

##### if表达式 #####

```python
# 在Python中也有类似C语言中的三目运算符
full_name = 'urain39
result = full_name if full_name.endswith('Zhang') else 'Guest'

print(result) # => Guest
```

##### 链式比较 #####

与其他语言不同的是Python里支持链式比较，这一点相比较其他语言可读性会有很高的提升。

```python
>>> x = 3
>>> 0 < x < 10
>>> True
```

不过与其链式比较最不匹配的莫过于等式赋值是没有返回值的，在C语言中你或许可以使用类似以下语法，但是在Python中这样的语法是不允许的。且不说Python没有`++`运算符，单就`x++`的返回值也是有问题的。**Python里`x++`的返回值一定是`None`**

```c
int main() {
    int x = 0;

    while (x != 10)
    	prinf("%d\n", x++);
}
```

##### is语句与“==” #####

> 用来检查两个对象是否相等，而is用来检查两个对象是否相同（是同一个对象）。 
>
> **警告：**不要将is用于数和字符串等不可变的基本值。鉴于Python在内部处理这些对象的方式， 这样做的结果是不可预测的。 (表示没能理解，谁语文好能解释一下？)

##### 字符串比较 #####

> 字符串和序列的比较 字符串是根据字符的字母排列顺序进行比较的。
>
> 涉及大写字母时，排列顺序就可能与你想要的不同，一个诀窍是忽略大小写。
>
> 为此可使用字符串方法lower，如下所示(参见第3章)：
>
> ```python
> >>> "a".lower() < "B".lower() True
> >>> 'FnOrD'.lower() == 'Fnord'.lower()
> True 
> ```

##### 逻辑运算符 #####

逻辑运算符有`and or not`，在使用if语句时可合并多个嵌套if语句。

##### 短路逻辑和表达式 #####

> 短路逻辑和条件表达式 布尔运算符有个有趣的特征：只做必要的计算。例如，仅当x和y都为真时，表达式`x and y`才为真。因此如果x为假，这个表达式将立即返回假，而不关心y。实际上，如果x为假，这 个表达式将返回x，否则返回y。（这将提供预期的结果，你明白了其中的原理吗？）这种行为 称为**短路逻辑**（或者**延迟求值**）：布尔运算符常被称为逻辑运算符，如你所见，在有些情况下 将“绕过”第二个值。对于运算符or，情况亦如此。在表达式x or y中，如果x为真，就返回 x，否则返回y。（你明白这样做合理的原因吗？）请注意，这意味着位于布尔运算符后面的代 码（如函数调用）可能根本不会执行。像下面这样的代码就利用了这种行为： `name = input('Please enter your name: ') or ''` 如果没有输入名字，上述or表达式的结果将为''。在很多情况下，你都宁愿使 用条件表达式，而不耍这样的短路花样。不过前面这样的语句确实有其用武之地。 

#### 断言assert ####

当我们有让程序在某个数值在安全范围内的情况下执行某段语句时，我们就可以用到assert语句。

```python
# 如当我们有需求在一个R18网站限制访问年龄时
# 我们就可以使用assert断言语句来拒绝某些访问。

age = 15
assert age > 18
```

当年龄小于18时程序会抛出一个**AssertionError异常**

#### 循环语句 ####

##### while循环 #####

简单实例：

```python
while True:
    print('Hello!')

while x < 10:
    x += 1
    print(x)
```

##### for迭代 #####

简单实列：

```python
words = ['Hello', 'World!']

for word in words:
    print(word)
```

else语句：

```python
# 当我们迭代循环时，假设我们需要在未break的分支加上一个默认操作
# 那么我们就可以使用for...else...语句来实现

for i in range(0, 100):
    print(i)
else:
    i += 1
    print(i)
# 以上语句将会输出0至100，其中如果去掉else分支那么将会输出0~99
```

##### 列表推导式 #####

> 列表推导是一种从其他列表创建列表的方式，类似于数学中的集合推导。列表推导的工作原
> 理非常简单，有点类似于for循环。

```python
# 简单的列表推导式
[x * x for x in range(10)] # -> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 较复杂的列表推导式
[(x, y) for x in range(3) for y in range(3)]
# -> [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 等价于
result = []
for x in range(3):
    for y in range(3)
        result.append((x, y))
```

推导式中也可以包含有if语句

```python
[x for x in range(1, 100) if x % 2 == 0] # -> 返回所有被2整除的数
```



#### 扩展阅读与本章总结 #####

[扩展阅读与本章总结](扩展阅读与本章总结.md)

