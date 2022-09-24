# 1.生成器：返回特殊迭代器的函数（定义迭代器）

# instance of Generator and Iterator
# 惰性
def num_generator():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')
    # for i in range(10):
    #     print('start {}'.format(i))
    #     yield i
    #     print('end')

# 不会输出任何东西，只有在遍历该迭代对象时才会真正调用生成器函数：  生成器表达式
n_generator = ( i*2 for i in num_generator())
# 使用列表生成式时，会打印 start continue end，生成器函数会执行除yield之外所有的代码： 列表推导式
n_generator = [ i*2 for i in num_generator()] 

# 以上会得到一个生成器对象 Generator

# print(type(n_generator)) # <class 'generator'>
for j in n_generator:
    print(j)

import re
re.finditer # return a iterator object for each match string
# iter1.send(value) 获取生成器返回值并传值


# 2.迭代器: 由__next__和__iter__函数组成 
# 其中：__iter__ 返回自身，__next__ 返回元素
# 只有__iter__ 方法是可迭代对象，不是迭代器和生成器
# NumIter:<perent class: Iterator>

from reprlib import recursive_repr
class NumIter:
    data = []
    def num_generator():
        for i in range(10):
            
            yield i
    
    def __init__(self) -> None:
        self.data.append(123)
        self.data.append(456)
        self.data.append(789)


    def __iter__(self):
        # 实例变成可迭代对象
        yield from range(11,20)
        # return self

    def __getitem__(self, index):
        # 支持索引取值
        return self.data[index]

    def __next__(self):
        # 结合__iter__实现迭代器Iterator的抽象接口
        if len(self.data) == 0:
            raise StopIteration
        else:
            n = self.data[0]
            del self.data[0]
            return n

    def __repr__(self):
        # print(instance) 打印实例对象时输出的内容
        return '{0} {1}'.format(self.__class__,self.data)

from collections import abc
num_iter = NumIter()

print(num_iter)

for i in num_iter:
    print(i)


# 3.可迭代对象：能顺序遍历该对象，如list,set,tuple,dict


# 改进：惰性生成器写法：

# 生成器函数
# 注意：若执行list(generator) 如果生成没有终止值，则有可能会一直生成(next(generator))，直到内存耗尽
import itertools
def gen_num(start, step, end=None):
    # 强制转换类型，start和step的类型可能不同
    new_start = type(start + step)(start)
    gener = itertools.count(new_start, step)
    if end is not None:
        gener = itertools.takewhile(lambda n: n < end, gener)
    return gener

def num_generator(start, step, end=None):
		index = 0
		result = type(start + step)(start)
		
		while end is None or result< end:
				yield result
				index += 1
				result = start_new + step * index
# 迭代器模式:
"""
为了实现多种遍历方法将可迭代对象和迭代器分开实现
如：
Number类只实现遍历方法__iter__ 返回迭代器对象NumberGenerator
NumberGenerator类实现 __iter__ 和 __next__ 
这样做在对不同条件遍历提供接口
迭代器模式可用来： 

访问一个聚合对象的内容而无需暴露它的内部表示

支持对聚合对象的多种遍历

为遍历不同的聚合结构提供一个统一的接口（即支持多态迭代）为了“支持多种遍历”，
必须能从同一个可迭代的实例中获取多个独立的迭代器，而且各个迭代器要能维护自身的内部状态，
因此这一模式正确的实现方式是，每次调用 iter(my_iterable) 都新建一个独立的迭代器。
这就是为什么这个示例需要定义 NumberGenerator 类。

"""

import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Number:
    
    def __init__(self, start, step, end=None) -> None:
        self.start = type(start + step)(start)
        self.step = step
        self.end = end
    
    def __iter__(self):
        return NumberGenerator(self.start, self.step, self.end)

class NumberGenerator:

    def __init__(self, start, step, end=None):
        self.start = start
        self.step = step
        self.end = end
        self.index = 0

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        # 返回可迭代对象
        # 
        return self
    
    def __next__(self):
        
        num = self.start + self.step * self.index
        self.index += 1
        if num > self.end:
            raise StopIteration
        return num
        

    def __repr__(self) -> str:
        repr_str = '{} is Generator? {}\n{} is Iterator ? {}\n'.format(self.__class__, isinstance(self, abc.Generator),self.__class__, isinstance(self, abc.Iterable))
        return repr_str


number_gen = NumberGenerator(0,0.5,5)
number = Number(0,0.5,5)
# iter(number) 重新构建一个新的迭代器，即调用一次number.__iter__()方法
print('iter1.....................')
iter1 = iter(number)
for item in iter1:
    print(item)
print('iter2.....................')
iter2 = iter(number)
for item in iter2:
    print(item)





'''
 生成器方法:
   __next__():  获取下一个元素
  send(value): 向每次生成器调用中传值 注意： 第一次调用send(None)
  
'''


def gen():
    i = 0
    while i < 5:
        temp = yield i  # return 1 + 暂停
        print('temp:', temp)
        for x in range(temp):
            print('--------->', x)
        print('****************')
        i += 1
    return '没有更多的数据'


g = gen()

# print(next(g))
# print(next(g))
# print(next(g))

# g.__next__()
print(g.send(None))
n1 = g.send(3)
print('n1:', n1)
n2 = g.send(5)
print('n2:', n2)
