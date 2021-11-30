# 36. 两列表有序合并 不允许使用extend
# 即合并后还是按顺序排序
l1 = [1,2,3,4]
l2 = [1,2,5,659]
#  -> [1,1,2,2,3,4,5,676]
#l1.extend(l2)

# 使用辅助的方法
def merge_list(list1,list2):
    l3 = list1 + list2
    return sorted(l3, key=lambda x: x)

# 不适用任何辅助方法

def merge_list_origin(list1,list2):
    new_list = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] > list2[0]:
            new_list.append(list2[0])
            del list2[0]
        else:
            new_list.append(list1[0])
            del list1[0]

    while len(list1) > 0:
        new_list.append(list1[0])
        del list1[0]
    
    while len(list2) > 0:
            new_list.append(list2[0])
            del list2[0]

    return new_list
    


print(merge_list(l1,l2))
print(merge_list_origin(l1,l2))


