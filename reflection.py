class Foo(object):
    def hello(self):
        return 'hello'


# without reflection
obj = Foo()
obj.hello()

# with reflection
class_name = "Foo"
method = "hello"
obj = globals()[class_name]()
getattr(obj, method)()

# with eval
eval("Foo().hello()")

"""
反射的意义：
不使用反射同样可以实现根据不同的需求进行不同的调用，但是这样就需要写大量类似if，else的语句。而且仍然需要内省机制的配合。
反射提供了一种更优雅的方式来实现这个特性。
"""

"""
reference

学习java应该如何理解反射？ - 老顽童周伯通的回答 - 知乎
https://www.zhihu.com/question/24304289/answer/147529485

sczyh30 (2015-06-24) 深入解析Java反射（1） - 基础
https://www.sczyh30.com/posts/Java/java-reflection-1/
"""