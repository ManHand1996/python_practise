# 36. 两列表有序合并 不允许使用extend
# 即合并后还是按顺序排序
l1 = [1,2,3,4]
l2 = [1,2,5,659]
#  -> [1,1,2,2,3,4,5,676]
#l1.extend(l2)

# 1.使用辅助的方法
def merge_list(list1,list2):
    l3 = list1 + list2
    return sorted(l3, key=lambda x: x)

# 2.添加然后删除原列表内容

def merge_list_origin(list1,list2):
    # 当两列表数量达到10w时
    # runtime： 6.192 seconds

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
    
# 3.从两列表第一个元素开始比较，然后往前移动。直到其中一个列表遍历完
def merge_list_origin2(list1,list2):
    # 当两列表数量达到10w时
    # runtime： 0.992 seconds
    i = 0
    j = 0
    list3 = []
    while True:
        if list1[i] > list2[j]:
            list3.append(list2[j])
            j += 1
        else:
            list3.append(list1[i])
            i += 1
        if j == len(list2) or i == len(list1):
            break
    
    # 从当前index开始添加

    for x in range(i,len(list1)):
        list3.append(list1[x])
    
    for y in range(j, len(list2)):
        list3.append(list2[y])

    return list3
    
l1 = [1,3,5,7,8,9]
l2 = [4,5,6,7,10]
# print(merge_list(l1,l2))
print(merge_list_origin(l1,l2))

l3 = [1,3,5,7,8,9]
l4 = [4,5,6,7,10]
print(merge_list_origin2(l3,l4))



