# 41 super函数的具体用法和场景
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p07_calling_method_on_parent_class.html

# 类继承顺序 MRO


# C -> A
# C -> B
# 先继承A，所以在C中调用父类同名方法会先使用A的方法
class A:
    def __init__(self) -> None:
        pass
    def get_classname(self):
        print(A)

class B():
    def __init__(self) -> None:
        # 确保父类正确初始化
        super().__init__()

    def get_classname(self):
        print(B)

class C(A,B):

    @classmethod
    def clsm(cls):
        pass

    def __init__(self) -> None:
        super().__init__()
        super().get_classname()
        print(type(C.clsm))
        

c = C()
