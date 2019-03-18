"""
Python functools partial
partial 的意思是局部 这里可以看到一点闭包的样子了

def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfun

"""
import string
from functools import partial

v = int('1101')
print(v)

v = int('1101', base=2)
print(v)

base2 = partial(int, base=2)
v = base2('1101')
print(v)


def outer(n):
    n += 1

    def inner(x):
        return x ** n

    return inner


f = outer(3)
print(f(2))
print(f(2))
print(f(2))

# partial 属于闭包(closure)的限制应用

# decorator 同样属于闭包 decorator就是closure的outer部分

"""
关于partial的使用意义
higher-order function，高阶函数可以传递函数作为参数和返回值。
如果函数1对函数2产生了影响后，又函数3讲函数2作为参数继续执行时候，这些影响在函数1和3之间是怎样传递的，或者说是如何保存在函数2中的。
在OOP中，参数作为实例变量被保存下来，对实例的作用，作用在了这些变量的状态上，状态在实例生命周期内被保存在方法间传递。
而在FP中，则是以partial的方式被传递。function -trans-> function 
"""


class Foo(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'


def upper_foo_a(instance: Foo) -> Foo:
    instance.a = instance.a.upper()
    return instance


def foo(a='a', b='b'):
    return a + b


def upper_foo_b():
    def foo(a='a', b='B'):
        return a + b

    return foo


# 这个例子不太精确，仅仅表达到此为止的观点。



"""
Reference

Python (v3.6.8) functools — Higher-order functions and operations on callable objects 
https://docs.python.org/3.6
Retrieved March 18, 2019 from https://docs.python.org/3.6/library/functools.html#functools.partial 

suninf (Aug 10, 2012) Python之函数式编程 
https://www.suninf.net
Retrieved March 18, 2019 from https://www.suninf.net/2012/08/function-in-python.html

the5fire (2014-01-13) python中functools宝库下的partial
https://www.the5fire.com
Retrieved March 18, 2019 from https://www.the5fire.com/python-functools-partial.html
"""
