"""
写出单例模式：

为什么是单例模式：
确保在程序中有且只有一个实例对象，通过类调用公共对象

"""

class SingeltonBase(object):
    # 基类实现单例
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls,*args, **kwargs)
        return cls._instance


class Foo(SingeltonBase):
    pass
f1 = Foo()
f2 = Foo()
print(f1 is f2)
print(f1)
print(f2)
# output: 两个对象指向同一地址，即是同一个对象
# True
# <__main__.Foo object at 0x0000000003792580>
# <__main__.Foo object at 0x0000000003792580>