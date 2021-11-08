"""
列表生成式：写出公差为N的等差数列(10个)，从1开始： 1,1+n，1+2n
"""
n = int(input("> 公差：\n"))
l = [1 + (i-1) * n for i in range(1,10)]
print(l)