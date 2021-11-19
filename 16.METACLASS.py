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

print(hasattr(person,'foo'))
p2 = person2()
print(p2.FOO)

