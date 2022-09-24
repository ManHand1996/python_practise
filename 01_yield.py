#-*-coding:utf-8 -*-
from mmap import mmap

from sqlalchemy import true
"""
    Q：读取10G大文件，现在只有4G内存 如何做？

    方案： yield 将函数变成生成器，分次读取，只要限制好每次读取的大小就能够完成.
    知识点：
    yield 关键字使函数变成生成器，能在程序运行时(需要时)生成相应数据，而不是一开始就定义好。
    像读取一个比较大的列表数据，
    若一次过读取则会有内存限制问题，
    注意需要限制好读取次数不然会在读取上花太多时间

    *换行一次，则读取的行数会+2
"""
def test_yield():
    print('test_yield..')
    global lines
    lines = 0
    data = []
    with open('yield_file2.txt','rb') as f:
        d = f.readlines(1000)
        data.append(d)
        yield data

def test_yield2(lines_read):
    data = []
    with open('yield_file2.txt','r+') as f:
        file_map = mmap(f.fileno(), 0)
        print('lines:' ,len(file_map))
        row = 0
        for i,char in enumerate(file_map):
            if char == b'\n':
                data.append(file_map[row:i+1].decode())
                row = i + 1
            if data.__len__() == lines_read:
                yield data
                data.clear()
# f = test_yield(200)



# for data in test_yield2():
#     print(data)

# with open('yield_file2.txt','w+') as f:
#     for i in range(0,200000):
#         f.writelines(str(i)*10 + "\n")


# for data in test_yield2(1000):
#     print(data)


def gen_num():
    r = 0
    while true:
        r += 1
        try:
            n = yield r
        except GeneratorExit:
            pass
        
g = gen_num()
g.send(None)
for i in g:
    if i == 5:
        r = g.close()
        print(r)
        