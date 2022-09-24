

from pympler import asizeof

import weakref
import timeit
import sys

class C:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

class Foo:
    __slots__ = ['id', 'name', '__weakref__']
    
    def __init__(self,id, name) -> None:
        self.id = id
        self.name = name

class Foo_C(Foo):
    pass

c = C(1,'myname')
bar = Foo(2, 'yourname')
bar_c = Foo_C(3, 'hername')
# 除非定义了 '__weakref__' 否则不能使用若引用
bar_weak = weakref.ref(bar)
print(f'{C.__name__=}, {c.__dict__}, sizeof c {asizeof.asizeof(c)} ')
print(f'{Foo.__name__=},{bar.__slots__}, sizeof bar {asizeof.asizeof(bar)}')
print(f'{Foo_C.__name__=},{bar_c.__dict__}, sizeof bar {asizeof.asizeof(bar_c)}')
print(set(dir(bar)).difference(set(dir(c))))

"""
output:
C.__name__='C', {'id': 1, 'name': 'myname'}, sizeof c 352 
Foo.__name__='Foo',['id', 'name'], sizeof bar 144
Foo_C.__name__='Foo_C',{}, sizeof bar 256
{'__dict__', '__weakref__'}

总结：
1.__slots__ 能够有效地减少内存空间的浪费
2.只能访问__slots__定义的属性
3.__slots__ 不会被继承，需要显式指定__slots__ = [] + super.__slots__ 
4.除非在__slots__ 中定义了 '__weakref__' 属性，否则不能作为弱引用对象.
"""