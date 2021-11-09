"""
__new__(cls,*args,**kwargs) 函数

返回父级对象实例
作用：创建实例的静态方法，在 __init__() 前调用

"""

class test():
    value = 0
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print("use __new__ ")
        return instance

    def __init__(self, v):
        print("use __init__")
        self.value = v

a = test(2)
b = test(1)


