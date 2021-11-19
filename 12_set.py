l1 = [1,2,3]
l2 = [3,4,5]

# 差集
# l1 与 l2 的差集
print(set.difference(set(l1),set(l2)))

# l1 与 l2 的差集 和 l2 与 l1 的差集 => 两列表中不同的元素
print(set(l1) ^ set(l2))

# 交集 => 两列表相同元素
print(set(l1).intersection(set(l2)))
print(set(l1) & set(l2))

# 并集
print(set(l1) | set(l2))
print(type(set(l1).union(set(l2))))
print(type((1,)))