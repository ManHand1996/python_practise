#38.写一个函数找出一个整数数组中，第二大的数

import random
from functools import reduce

def solution1(num_list:list):
    '''
    1.solution 1：
    sorted(list)
    return list[1]
    '''
    num_list.sort(reverse=True)

    return num_list[1]

def solution2(num_list:list):

    '''
    2. solution 2
    设置 一个最大值first_max, 一个次最大值second_max
    遍历元素 num in num_List：
        if num > first_max: 交换最大值和次最大值 -> second_max = first_max ;first_max = num;
        else if num > second_max : 交换次最大值 ->  second_max = num 
    '''

    first_max = num_list[0]
    second_max = num_list[0]

    for num in num_list:
        
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max:
            second_max = num
    return (first_max, second_max)

def solution3(num_list:list):
    '''
    3. solution3
    使用functools.reduce(function,iter[,init])函数
    # 表达式 True and (value) 
    # 若关系表达式最后跟着值（对象）的是非BOOL值（对象）
    # 则返回时会 返回该值

    # reduce 对可迭代对象的第一个，和第二个元素进行操作，
    # 可以初始化第一个元素的值，若初始化，而第二个参数从可迭代对象开始获取
    # 返回第一个参数迭代后的值
    # 
    '''
    return reduce(lambda x,y:  y > x[0] and (y, x[0]) or y > x[1] and (x[0], y) or x ,num_list,(num_list[0],num_list[0]))


num_list = [ random.randint(i,1000) for i in range(10)]
num_list = [146, 749, 611]
num_list2 = [146, 749, 611]

print(id(num_list))
print(id(num_list2))

print(num_list)
# print(solution1(num_list))
# print(solution2(num_list2))
print(solution3(num_list2))

def test():

    return 1 > 0 and int

print(test())
