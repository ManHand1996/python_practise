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