# 3. 元类 创建单例模式
"""
元类，METACLASS, 在python中是用于创建类的类，类可以创建实例，而元类可以创建类,：如type(classname:str, parent_classs:tuple, attrs:dict)
类在python中也是对象
"""

# __metaclass__

# metaclass : 函数
def upper_attr(class_name, class_parents, class_attr):
    '''Return a class object, with the list of its attribute turned into 
    uppercase.
    '''
    # pick up any attribute that doesn't start with '__' and turn it into uppercase.
    uppercase_attr = {}
    print(class_parents)
    for name, val in class_attr.items():
        if name.startswith('__'):
            uppercase_attr[name] = val
        else:
            uppercase_attr[name.upper()] = val
    
    # let `type` do the class creation
    return type(class_name, class_parents, uppercase_attr)


class person2(metaclass=upper_attr):
    
    foo = 'AAVccc'


# metaclass : 类
class UpperCase(type):

    def __new__(cls,cls_name, parents_cls, attrs):
        # 改写创建的实例对象内容
        # 所有对象都用type创建

        # type(classname:str, parent_classs:tuple, attrs:dict)

        attrs = ((name, value) for name, value in attrs.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        # cls: ->self -> type

        return super(UpperCase, cls).__new__(cls,cls_name,parents_cls,uppercase_attr)


class person3(metaclass=UpperCase):
    
    foo = 'AAVccc'

print(hasattr(person3,'foo'))
p3 = person3()
print(p3.FOO)


# 元类实现
# metaclass 是 type 的子类
# 定义类时，实际上执行 MyMeta = Type(classname, superclasss, classattr)
# 通过替换 type 的 __call__ 运算符重载机制，“超越变形”正常的类

# 运行顺序
# Meta.__new__
# Meta.__init__
# 实例化子类时Meta.__call__
class MyMeta(type):
    
    def __init__(self, name, bases, dic) -> None:
        """
        name:str metaclass的子类
        bases:tuple metaclss子类的一般继承父类
        dic:dict 类属性和方法
        """
        print('----- args name:',name)
        print('----- args bases:',bases)
        # 构造类名为参数name的类对象（并非类实例）
        super().__init__(name, bases, dic)
        print('>: MyMeta.__init__')
        print(self.__name__)
        print(dic)
        print(self.yaml_tag)

    def __new__(cls, *args, **kwargs):
        print('>:MyMeta.__new__')
        print(cls.__name__)
        return type.__new__(cls, *args, **kwargs)
    
    def __call__(cls, *args, **kwargs):
        print('>:MyMeta.__call__')
        obj = cls.__new__(cls)
        print('after MyMeta.__call__')
        cls.__init__(cls, *args, **kwargs)
        return obj

class BigFoo():
    
    cname = 'af'

    def __init__(self) -> None:
        self.bname = 'sff'
        print('BigFoo.__init__')

    @classmethod
    def showname(cls):
        print(cls.__name__)

    @staticmethod
    def showname_static():
        print('asfasfasfsa')

class Foo(BigFoo):
    yaml_tag = "!Foo"

    def __init__(self, name) -> None:
        print('Foo.__init__')
        super().__init__(self)
        self._name = name
    
    def __new__(cls, *args, **kwargs):
        print('Foo.__new__', )
        # 返回可调用对象
        #return cls

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,val):
        self._name = val

    @name.deleter
    def name(self):
        del self._name

    

# foo = Foo('foo00')
# print(foo.name)


class A:
    def __new__(cls):
        cls.__init__(cls)
        print(cls)
        print("A's __new__() invoked")

    def __init__(self):
        print("A's __init__() invoked")


class B(A):
    
    
    def __init__(self):
        
        print("B's __init__() invoked")
        self.name = 'asfs'
    
    def __new__(cls):
        print("B's __new__() invoked")
        # return super().__new__(cls)

b = B()

print(b)
# a = A()

class Human:
    def __getInfo(self):
        return "Human's getInfo is called"
class Person(Human):

    
    def __getInfo(self):
        return "Person's getInfo is called"
    
    def msg(self):
        return "Person msg."

    def printPerson(self):
        print(self.__class__)
        print(self.__getInfo(), end = ' ')
        print(self.msg(), end = ' ')
        
        
        

class Student(Person):

    

    def __getInfo(self):
        return "Student's getInfo is called"

    # def printPerson(self):
    #     print(self.__getInfo(), end = ' ')
    #     print(self.msg(), end = ' ')

    def msg(self):
        return "Student msg."

Person().printPerson()
Student().printPerson()