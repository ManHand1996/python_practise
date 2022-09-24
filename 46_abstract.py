'''
python 中的抽象类

1.对属性和方法进行预定义但不实现(实际上可以实现, 但一般都只进行定义)
2.抽象类不能实例化
3.一般情况单继承

抽象类概念：
1.不能实例化
2.单继承
3.对抽象方法，属性进行预定义，但也可以实现部分抽象方法
4.抽象类可以有非抽象方法
5.继承抽象类的类必须实现抽象类的定义的所有抽象方法, 不然会报错

'''
# 和接口类似
import abc #利用abc模块实现抽象类

class All_file(metaclass=abc.ABCMeta):
    all_type='file'
    @abc.abstractmethod #定义抽象方法，无需实现功能
    def read(self):
        '子类必须定义读功能'
        print('all_file class read')

    @abc.abstractmethod #定义抽象方法，无需实现功能
    def write(self):
        '子类必须定义写功能'
        pass
    
    @classmethod
    def hello(cls):
        print(cls.__name__, 'hello func')

class Txt(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        super(Txt, self).read()
        print('文本数据的读取方法')

    def write(self):
        print('文本数据的读取方法')

if __name__ == '__main__':
    # 如果没有实现抽象类的抽象方法,则初始化对象时会报错:
    # TypeError: Can't instantiate abstract class Txt with abstract methods write
    a = Txt()
    a.read()
    a.hello()