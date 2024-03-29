# 41 super函数的具体用法和场景
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p07_calling_method_on_parent_class.html

# 类继承顺序 MRO

# E <- A,B
# A <- C, B <- C
# 先继承A，所以在C中调用父类同名方法会先使用A的方法

# Python3 中MRO 为广度优先
class E():
    def __init__(self) -> None:
        print('init E')
    def get_classname(self):
        print(E)

class A(E):
    def __init__(self) -> None:
        super(A, self).__init__()
        print('init A')
    # def get_classname(self):
    #     print(A)

class B(E):
    def __init__(self) -> None:
        # 确保父类正确初始化
        super(B, self).__init__()
        print('init B')

    def get_classname(self):
        print(B)

class F(E):
    def __init__(self) -> None:
        # 确保父类正确初始化
        super(F,self).__init__()
        print('init F')

    def get_classname(self):
        print(B)

class C(B,A,F):

    name = 'public name' # 公有变量
    _protected_name = '_protected_name' # 类实例和子类实例可以访问
    __private_name = '__private_name' # 只能该类对象访问，类实例访问会报错

    # __xx__ 双下划线系统定义名字
    # 继承对象创建时会执行一次
    def __init__(self) -> None:
        # super().__init__()
        super(C, self).__init__()
        print('init C')
        # C.static_func()
    
    def __ffdel__(self):
        print('__del__')

    @classmethod
    def clsm(cls):
        # 类对象调用
        print('class method')
    
    @staticmethod
    def static_func():
        print('static method...')
        print(C.name)


        

c = C()
print(C.mro())
# c.static_func()
# c.clsm()
# print(c._protected_name)
#print(c.name)
# print(c.__private_name)
# print(c.name)
# print(c.__ffdel__())
# import inspect
#print(inspect.getmro(C))
#print(getattr(c, "static_func"))
#print(dir(c))
