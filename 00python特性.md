### 1. python3 可变类型和不可变类型

可变类型：list,dict
修改，都在同一内存地址中操作
```python
l1 = [1,2,3]
l2 = l2
l1.append(4)
>>> id(l1)
32428096
>>> id(l2)
32428096
```
不可变类型：string, number, tuple
修改时，会另外开辟内存进行操作，即创建了新的对象
```python
n1 = 123
n2 = n1
n2 += 1
>>> id(n1)
8791093945936
>>> id(n2)
8791093945968
# 但当n2 再进行减1，地址就会指向回n1,
# python 会存储常量地址，在复制变量时，会查找是否已经存在该常量
```

### 2. python 中变量的作用域
- 按LEGB查找

L: local 函数内部作用域
```
def func(arg):
    pass
```
E: enclosing 内嵌函数和函数内部之间
```

def func(name):
    # start
    def wraps(name2):
        pass
        # end 
```
G: golbal 全局

B: build-in 内置

### 3.Python 类中私有，保护表示

```python
class C(A,B):

    name = 'public name' # 公有变量
    _protected_name = '_protected_name' # 类实例和子类实例可以访问
    __private_name = '__private_name' # 只能该类对象访问，类实例访问会报错

    # __xx__ 双下划线系统定义名字
    # 继承对象创建时会执行一次
    def __init__(self) -> None:
        super().__init__()
        super().get_classname()
        C.static_func()
    
    def __ffdel__(self):
        print('__del__')

    @classmethod
    def clsm(cls):
        # 类对象调用
        pass
    
    @staticmethod
    def static_func():
        print('static method...')
        print(C.__private_name)
```

### 4. 接口类和抽象类