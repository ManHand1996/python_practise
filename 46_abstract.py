'''
python 中的抽象类

1.对属性和方法进行预定义但不实现
2.抽象类不能实例化
3.一般情况单继承

抽象类概念：
1.不能实例化
2.单继承
3.对抽象方法，属性进行预定义，但也可以实现部分抽象方法
4.抽象类可以有非抽象方法

'''
# 和接口类似
import abc #利用abc模块实现抽象类

class All_file(metaclass=abc.ABCMeta):
    all_type='file'
    @abc.abstractmethod #定义抽象方法，无需实现功能
    def read(self):
        '子类必须定义读功能'
        pass

    @abc.abstractmethod #定义抽象方法，无需实现功能
    def write(self):
        '子类必须定义写功能'
        pass


class Txt(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('文本数据的读取方法')

    def write(self):
        print('文本数据的读取方法')