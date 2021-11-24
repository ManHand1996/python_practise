# reduce(function,iteratable)

# 对可迭代对象的第一和第二个元素进行操作

# function(x,y)

# etc:
from functools import reduce
l1 = [1,2,3,4]

print(reduce(lambda x,y : x+y, l1))


class testC():
    name = ''
    def __init__(self,name) -> None:
        self.name = name


a_test = testC('a_test')
b_test = a_test
print(id(a_test)," - ", b_test.name)
print(id(b_test)," - ", b_test.name)
b_test.name = 'b_test'
print(id(a_test)," - ", b_test.name)
print(id(b_test)," - ", b_test.name)