"""
32
该函数的输入是一个仅包含数字的list,输出一个新的list，其中每一个元素要满足以下条件：
1、该元素是偶数
2、该元素在原list中是在偶数的位置(index是偶数)
"""

def getevenlist(num_list):
    '''
    num_list:[int]
    return []
    '''
    # new_list = []
    # for num in num_list:
    #     if num % 2 == 0 and num_list.index(num) % 2 == 0:
    #         new_list.append(num)
    # return new_list
    return [ num for num in num_list if num % 2 == 0 and num_list.index(num) % 2 == 0]


num_list = [x for x in range(10)]
print(getevenlist(num_list))