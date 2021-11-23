
# 反转一个整数

def reverseInt(number:int)->int:
    # 反转可迭代对象
    num_list = list(reversed(str(number)))
    new_num = ''.join(num_list)
    
    # 反转字符串方法1.
    # new_num = str(number)[::-1] 

    if -10 == number or number == 10:
        return 0

    if num_list[-1] == '-':
        return -int(new_num[:-1])
    else:
        return int(new_num)


a = 1260
print(reverseInt(a))