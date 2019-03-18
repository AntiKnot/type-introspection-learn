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
Reference

Python (v3.6.8) functools — Higher-order functions and operations on callable objects 
https://docs.python.org/3.6
Retrieved March 18, 2019 from https://docs.python.org/3.6/library/functools.html#functools.partial 

suninf (Aug 10, 2012) Python之函数式编程 
https://www.suninf.net
Retrieved March 18, 2019 from https://www.suninf.net/2012/08/function-in-python.html
"""
