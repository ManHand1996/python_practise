# 37.给定一个任意长度数组，实现一个函数
# 让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序，如字符串'1982376455',变
# 成'1355798642'


def solution(num_list):
    odd_list = []
    even_list = []
    for i in num_list:
        num = int(i)
        if num % 2 ==0:
            even_list.append(str(num))
        else:
            odd_list.append(str(num))
    
    even_list.sort(key=lambda x: int(x),reverse=True)
    odd_list.sort(key=lambda x: int(x),reverse=False)
    print(even_list)
    print(odd_list)
    return ''.join(odd_list) + ''.join(even_list)


def solution2(num_list):
    pass
    # 升序排序，奇数在前升序，偶数在后降序
    # 从后往前遍历
    # 遇到偶数则往最后一位插入，这样偶数就护是降序
    num_list.sort()
    j = 0
    print(num_list)
    for i in range(len(num_list)-1,-1,-1):
        if num_list[i] % 2 == 0:
            num_list.insert(len(num_list), num_list.pop(i))
            print(num_list)

    # 降序排序，奇数在前升序，偶数在后降序
    # 从后往前遍历
    # 遇到奇数则往第一位插入，这样奇数就护是升序
    # num_list.sort(reverse=True) 
    # for i in range(len(num_list)):
    #         if num_list[i] % 2 > 0:
    #             num_list.insert(0, num_list.pop(i))
    #             print(num_list)

    
    return num_list



#num_l = [42,1,52,12,9,4,7,0,8,2,4]

#print(solution(num_l))

num_l = [3,13,5,54,1,6,7,8]
solution3(num_l)
print(solution2(num_l))

