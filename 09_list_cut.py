"""
l = [1,2,3]
print(l[:10])
print(l[10:])

当列表切片时，使用index超过列表大小时并不会出错（indexError），而是输出[] 空列表，
只有单独使用获取列表元素，超过列表大小时才会出现indexError l[10]
"""