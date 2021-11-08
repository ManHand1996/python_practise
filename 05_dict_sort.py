#-*-coding:utf-8 -*-
"""
5.现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?

output: {'i':12,'a':24,'k':33,'g':52}
"""

"""
sorted(iteratable, key=None, reverse=False)
可以用与所有可迭代对象排序， key 排序对象 reverse =False 升序
"""

d= {'a':24,'g':52,'i':12,'k':12}
l = [5, 0, 6, 1, 2, 7, 3, 4]
n_d = sorted(d.items(),key = lambda x: x[1])
print(n_d)


n_l = sorted(l, key = lambda x: -x)
print(n_l)