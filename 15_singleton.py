"""
写出单例模式：

为什么是单例模式：
确保在程序中有且只有一个实例对象，通过类调用公共对象

使用情况：

需要重复做某事情，但不需要每次分配资源，
"""
# 1.基类实现单例
class SingeltonBase(object):
    
    _instance = None
    def __new__(cls, *args, **kwargs):
        # __new__() 静态方法在__init__ 前调用，可以在这里重写，并设置类静态属性
        if not cls._instance:
            cls._instance = super().__new__(cls,*args, **kwargs)
        return cls._instance

class Foo1(SingeltonBase):
    pass

# obj1 = Foo1()
# obj2 = Foo1()
# print(obj1._instance)
# print(obj2._instance)

# 2.装饰器实现单例模式
from functools import wraps
def SingletonDecorator(cls):
    instance = {}
    @wraps(cls)
    def process(*args, **kwargs):
        if cls not in instance:
           instance[cls] = cls(*args, **kwargs)
        
        print('instance len:',len(instance),cls)
        return instance[cls]
    return process

@SingletonDecorator
class Foo(object):
    a1 = 10
    a2 = 11
    def __init__(self,*args) -> None:
        # super().__init__(Foo,*args,**kwargs)
        print(args[0])
        self.a1 = args[0]
        self.a2 = args[1]


@SingletonDecorator
class Foo2(object):
    a1 = 10
    a2 = 11
    def __init__(self,*args) -> None:
        # super().__init__(Foo,*args,**kwargs)
        print(args[0])
        self.a1 = args[0]
        self.a2 = args[1]
f1 = Foo(10,240)
f2 = Foo(20,205)
f3 = Foo2(20,205)
f4 = Foo2(20,205)


i1 = 10
print(type(type.__class__))
print(i1.__new__)
print()
# <class 'type'>
# <class 'int'>

print(f1 is f2)
print(f3 is f4)

# output: 两个对象指向同一地址，即是同一个对象
# True
# <__main__.Foo object at 0x0000000003792580>
# <__main__.Foo object at 0x0000000003792580>