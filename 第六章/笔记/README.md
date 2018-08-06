# 第六章 #



## 朝花夕拾 ##

```python
name = ['urain39', '95e2', 'suco']
n = name[:]

n is names # -> False
n == names # -> True

# 序列[:] -> 返回一个序列的副本

>>> x = 1
>>> y = x
>>> x is y
True

# 其他情况下赋值操作等于修改引用实际还是相等的
```

## 基础概念 ##

- Python函数中的参数是不可变的

  ```python
  >>> x = 0
  >>> def f(x): x = 3
  >>> f()
  >>> X
  0
  
  # 修改的值必须通过return返回
  ```

  **注意：如果x是一个列表，那么列表内的元素依旧是能够修改的**



- 关键字参数使用与默认值

  > 有时候，参数的排列顺序可能难以记住，尤其是参数很多时。为了简化调用工作，可指定参数的名称。 

  ```python
  # 简单的关键字参数函数
  def f(x=0, y=0):
      return x*y
  
  # 调用方法1
  f(1,2) # -> 2
  
  # 调用方法2(1)
  f(x=1, y=2) # -> 2
  
  # 调用方法2(2)
  f(y=2, x=1) # -> 2
  
  # 调用方法3
  f() # -> 0
  
  # 比较以上方法会发现在参数过多的情况下关键字参数函数
  # 会比普通参数函数具有更好的可阅读性，且可以指定默认值
  ```

  **注意：通常不应结合使用位置参数和关键字参数，除非你知道这样做的后果。一般而言，除非必不可少的参数很少，而带默认值的可选参数很多，否则不应结合使用关键字参数和位置参数。** 



- 收集参数与分配参数

  ```python
  # 当我们需要处理不定长度的多个参数时我们可以用到“*”和“**”符号
  # 这个概念有点类似于C语言里的可变长参数，但比可变长参数高级许多
  
  def speak(*words):
      for word in words:
          print(word)
  
  speak('Holy', 'F**k', 1, 2, 3) # => 'Holy\nFuck\n1\n2\n3'
  
  # 通过上面这段小程序你或许也猜到了“*”号能收集参数了
  # 那么我们能不能反过来将列表作为参数传入函数呢？答案当然是能的！
  
  words = ['Holy', 'Motherf**k']
  speak(*words) # => 'Holy\nMoterf**k\n'
  
  # 我们可以在传参时使用“*”作为分配运算符，对words进行解包
  
  # 除了序列以外，字典也是支持以上两种操作的
  def speak(**profile):
      print(profile.get('name'), profile.get('age'))
  
  def show_profile(name='Guest', age=0)
      pass
  
  profile = {
      'name': 'urain39',
      'age': 10
  }
  show_profile(**profile)
  ```

  

- Python中的作用域

  > 可将变量视为指向值的名称，这几乎与使用字典时一样（字典中的键指向值），只是你使用的是“看不见”的字典。这种“看不见的字典”称为**命名空间**或**作用域**。那么有多少个命名空间呢？除全局作用域外， **每个函数调用都将创建**一个。 

  ```python
  >>> def foo(): x = 42
  ...
  >>> x = 1
  >>> foo()
  >>> x
  1 
  
  # foo函数与外部x并不在同一作用域，好比两个字典里有一个
  # 名为“cat”的键，虽然两个键相同但是指向的数值确实千差万别
  ```

  

- 访问并修改局全局变量

  ```python
  # 在引入作用域的概念以后我们时常会访问本地变量以外的变量
  # 如上面所示我们已经知道了全局变量的名字能与本地变量重名
  
  x = 0
  def f():
      x = 3
  	# 访问局部变量时可以通过locals()函数返回的字典访问局部变量
  	locals('x') # -> 3
  	# 访问全局变量时可以通过globals()函数返回的字典进行全局变量
      globals('x') # -> 0
      # global x
      # SyntaxError: name 'x' is assigned to before global declaration
  
  def f1():
      # 绑定全局变量
      global x
      return x # -> 0
  ```

  

## 本章学习的函数 ##

- reduce函数

  ```python
  >>> from functools import reduce
  >>> reduce(lambda x,y: x * y, range(0, 100 + 1))
  5050
  
  # 用法：reduce(func, seq[, initial])
  # reduce函数用于完成重复的某件事，如上面的阶乘实现
  # 可作为函数递归的替代方法，不过一般很少使用这个函数
  # 如果提供了initial，且seq为空则返回initial
  ```

- sum函数

  ```python
  >>> sum(range(0, 100+1))
  5050
  
  # 用法：sum(seq)
  # 字面理解，传入一个数字序列返回序列元素累加结果
  ```

  

- map函数

  ```python
  >>> m = map(lambda x: print(x & 32), range(0, 100 + 1))
  list(m)
  # 用法：map(func, seq, [seq, ...])
  # 对序列中的所有元素执行函数func
  ```

  **注意：**Python3中的map函数与range函数已经从函数改成了类，也就是说在Python2中的map函数在执行时可以得到的数值而在Python3中将以对象存在，当正真需要时才会与运算。所以上面的示例在Python3环境下返回的只是一个iterable对象。使用l诸如tuple和list方法(对象)可以转换执行。

- filter函数

  ```python
  >>> f = filter(x > 3, [1, 2, 3])
  list(f)
  # 用法：filter(func, seq)
  # 对序列中的每一元素执行func，返回处理结果为真的元素序列
  ```

  

- lambda表达式(匿名函数)

  ```python
  # lambda表达式又名匿名函数是一个没有名字的与函数
  # 常用在当我们需要一个简单明确的函数时，也方便在内建函数
  # 诸如以上map和filter等函数中使用
  
  # 你也可以将匿名函数赋值给变量，使其成为“有名字”的函数
  
  # 用法示例：
  f = lambda x, y: x + y
  f(1, 2) # -> 3
  
  f = lambda x: x ** 3
  f(2) # -> 8
  ```

  

