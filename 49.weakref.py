import weakref

'''
弱引用
https://yuerblog.cc/2018/08/28/python-weakref-real-usage/

规则
1.不会对对象的引用计数产生影响
2.弱引用对象不能为int ,string, dict, list 
3.set和类对象可以

为什么有弱引用？
弱引用对内存管理有重要作用
1.解决循环引用
2.数据库连接池(不是太懂) https://www.zhoulujun.cn/html/theory/ComputerScienceTechnology/network/2015_0708_65.html

本质：
使用观察者模式
栈区                   堆区
a ->                     100
werk_b ->a

werk_b 观测 a



'''
import gc
def drop(obj):
    del obj
    print('del..')

class Test():
    pass

s1 = Test()
s2 = s1

wks1 = weakref.ref(s1, drop)


print(s1)
print(s2)

print(s1)
print(wks1())




