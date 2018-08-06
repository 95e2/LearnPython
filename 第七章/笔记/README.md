# 第七章 #



## 面向对象的特征 ##



- 多态：可对**不同类型的对象**执行**相同的操作**。
- 封装：对外部**隐藏**有关对象的工作原理的**细节**。
- 继承：可基于通用类创建**专用类**。



<!-- 第七章，117页 7.1 -->

## 私有方法 ##

> **Python没有为私有属性提供直接的支持**，而是要求程序员知道在什么情况下从外部修改属性 是安全的。毕竟，你必须在知道如何使用对象之后才能使用它。 要让方法或属性成为私有的（不能从外部访问），只需让其名称以两个下划线打头即可。 



```python
class Secretive:
	def __inaccessible(self):
 	print("Bet you can't see me ...")
 	def accessible(self):
 	print("The secret message is:")
 	self.__inaccessible() 
```



在类定义中，对所有以**两个下划线**打头的名称都进行转换，即在开头 加上一个下划线和类名。 

`Secretive._Secretive__inaccessible`只要知道这种幕后处理手法，就能从类外访问私有方法，然而不应这样做。 

> 如果你不希望名称被修改，又想发出不要从外部修改属性或方法的信号，可用一个下划线打 头。这虽然只是一种约定，但也有些作用。例如，from module import *不会导入以一个下划线 打头的名称①。 



##  类级变量和对象属性 ##

```python
class Person(object):
    count = 0
    def __init__(self):
        # __class__属性可能只存在于新式类中
        self.__class__.count += 1

p1 = Person()
p2 = Person()
p1.count      # -> 2
p2.count      # -> 2
Person.count  # -> 2
```

**类级变量属于类而不属于实例化以后的对象本身**，但实例化后的对象可以访问类级变量。但假设实例化对象中的属性中含有相同名字的变量，则优先返回属性中的变量。如：

```python
p3 = Person()
p3.count		# -> 3
p3.count = 99
p3.count 		# -> 99
Person.count 	# -> 3
```

## 类的继承与扩展 ##

在声明类时，类名后加上括号写明类名即可指定超类（父类）

```python
class Parent(object):
    def __init__(self):
        pass
	def sayHello(self):
        print('Hello, World!')

class Child(Parent):
    def __init__(self):
        # 重写父类“构造方法”
        super(self.__class__).__init__(self)

c = Child()
c.sayHello()
# 子类会继承父类中的方法，如果子类方法与父类方法
# 重名，即被认为是子类对父类方法的重写。
```

使用`issubclass`和`isinstance`方法可以用于判断子类，对象和父类的关系。

```python
# 判断子类是否为父类的子类
issubclass(Child, Parent) # -> True
issubclass(Parent, Child) # -> False

# 判断实例化对象是否为类的对象
isinstance([1, 2, 3], dict) # -> True
isinstance((1,), dict) # -> False
```

**注意**：尽管`isinstance`有能够判断对象类型的能力，但是`isinstance`在处理多继承的类型时会显得力不从心，如`MyDict`类型从dict继承，那么`MyDict`实例化的对象也都是dict类型。推荐的判断方法应该是通过新式类中的`<object>.__class__`属性来判断类型。



## 类的多继承 ##

本质上Python中的继承机制时将父类的方法与类属性附加于子类，所以如果同时继承多个类也是可以实现的。然而，除非万不得已，否则应避免使用多重继 承，因为在有些情况下，它可能带来意外的“并发症”。 



## 抽象基类

> 在历史上的大部分时间内，Python几乎都只依赖 于鸭子类型，即假设所有对象都能完成其工作，同时偶尔使用hasattr来检查所需的方法是否存 在。很多其他语言（如Java和Go）都采用显式指定接口的理念，而有些第三方模块提供了这种理 念的各种实现。最终，Python通过引入模块abc提供了官方解决方案。 

**简而言之**：抽象类是未具体实现的类，用于统一类的接口。

```python
from abc import ABC, abstractmethod

class Number(object):
    # 使用装饰器修饰方法为抽象方法
    @abstractmethod
    def get_int(self):
        pass
```

像以上的`Number`类并没有具体实现，只有方法框架就是抽象类。抽象类因为没有具体实现故不能有实例化对象，基于抽象类扩展的具体实现类才能够实例化对象。**抽象类里能含有具体实现的方法**。



## 本章学习的新函数与方法 ##



|             函数              |               描述               |
| :---------------------------: | :------------------------------: |
|         callbale(obj)         | 判断对象是否可调用（方法或函数） |
| getattr(obj, name[, defualt]) |   获取对象属性值，可提供默认值   |
|      hasattr(obj, name)       |     判断对象是否存在指定属性     |
|   isinstance(object, class)   |     判断对象是否是指定的类型     |
|      random.choice(seq)       |     随机返回列表中的一个元素     |
|   setattr(obj, name, value)   |  将对象的指定属性设置为指定的值  |
|           type(obj)           |          返回对象的类型          |

