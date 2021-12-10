'''
47.获取和设置属性

setattr(obj, attr_name, value)

getattr(obj, attr_name)

'''

class Test():
    def __init__(self) -> None:
        pass

t = Test()
# 为实例对象动态添加属性
setattr(t, 'name','tt')
print(getattr(t,'name'))


