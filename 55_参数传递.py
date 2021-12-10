'''
python 函数中参数传递：
1.值传递(对源对象不改变)
2.引用传递(引用传递)

'''

G_A = 100


# 值传递：一些常量如字符串，数字，在函数内部会重新分配栈区保持临时变量，对原数据不会有影响
def pass_by_value(a:int):
    global G_A
    a = 100
    G_A = 122
    print(G_A)
    print('a in func:{}'.format(a))

# 引用传递：dict，list等对象，将该对象的引用计数加1，并由临时变量指向，对原数据会有影响
# 本质上对函数的参数来说，其实也是值传递，将值（指向对象的地址）复制一份到参数上，修改参数为None但不会对原参数影响
def pass_by_ref(b:list):
    
    # b.append(1992)
    print('b in func:{}'.format(b))


a = 1
b = [1,2,3]

pass_by_value(a)
pass_by_ref(b)

print(a)
print(b)
print(globals())