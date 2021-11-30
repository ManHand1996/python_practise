"""
l = [1,2,3]
print(l[:10])
print(l[10:])

当列表切片时，使用index超过列表大小时并不会出错（indexError），而是输出[] 空列表，
只有单独使用获取列表元素，超过列表大小时才会出现indexError l[10]
"""

l1 = [x for x in range(11)]

# 列表切片形式：
# 1.list[start:end] -> 返回index start 至 (end-1) 的元素

# 2.list[start:end:step] step != 0  返回index start 至 (end-1) 的元素，并且元素在该返回的列表的步长为step:
# l = [0,1,2,3,4,5,6]
# l[::2] -> [0,2,4,6]

# 3. start 和 end 可以为负数，表示从列表最后开始查找
