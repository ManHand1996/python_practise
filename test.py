

# # def decorator22(func):
# #     print('start decorator22')
# #     def wrapper(*args):
        
# #         if args is not None:
# #             newargs = tuple([x+1 for x in args])
# #         x = func(*newargs)
# #         print('end decorator22')

# #         return x

# #     return wrapper

# # def decorator2(func):
# #     print('start decorator2')
# #     def wrapper2(*args):
        
        
# #         if args is not None:
# #             newargs = tuple([x+1 for x in args])
# #         x = func(*newargs)
# #         print('end decorator2')

# #         return x
# #     return wrapper2


# # # if decoraotr no args, default one argment => function name

# # @decorator22
# # @decorator2
# # def test2(*args):
# #     print('test2')
# #     print(args)
# #     return args[0]

# # # define decorator sequence:
# # #test2 = decorator2(test2)
# # #test2 = decorator22(test2)

# # # execute decorator sequence:
# # # decorator22.wrapper
# # # decorator2.wrapper
# # test2(10)

# # from genericpath import exists
# # import os
# # def findFileWithWalk(root_path, suffix):
# #     files_list = []
# #     for path,path_names, filenames in os.walk(top=root_path):
# #         for filename in filenames:
# #             # if filename.find(suffix) >= 0:
# #             #     print(os.path.join(path,filename))
# #             # name,suf =os.path.splitext(filename)
# #             # if suf == suffix:
# #             #     print(os.path.join(path,filename))
            
                
# #             files_list.append(os.path.join(path,filename))
# #     return files_list

# # findFileWithWalk('/home/manhand/Pictures','png')


# # def copyFolder(srcPath,tarPath):
# #     files_list = findFileWithWalk(srcPath,'')
# #     for filename in files_list:
# #         with open(filename, 'rb') as readStream:
# #             content = readStream.read()
            
# #             target_file = filename.replace(srcPath, tarPath)
# #             target_path = os.path.dirname(target_file)
            
# #             if not os.path.exists(target_path):
# #                 os.mkdir(target_path)
            
# #             with open(target_file, 'wb') as writeStream:
# #                 writeStream.write(content)

# # # copyFolder(r'/home/manhand/Pictures', r'/home/manhand/Music')

# # import re
# # a = re.search(r'[^/]+\.[\w]+','/home/manhand/Pictures/wallpapers/Waves Dark 6016x6016.jpg')
# # print(a[0])

# # try:
# #     a = 1 + '234'
# #     a = int(a)
# # except Exception as e:
# #     print(e)
# # finally:
# #     print('done')

# # from typing import overload


# # @overload
# # def process(response: None) -> None:
# #     print('using None')
# #     return None

# # @overload
# # def process(response: int) -> tuple[int, str]:
# #     print('using int')
# #     return (1,'process')

# # @overload
# # def process(response: bytes) -> str:
# #     print('using bytes')
# #     return 'process bytes'

# # def process(response):
    
# #     pass

# # process(23)

# from functools import reduce
# from random import random


# def decorator22(func):
#     print('decorator22')
    
#     def wrapper(*args):
#         print('start decorator22')
#         if args is not None:
#             newargs = tuple([x+1 for x in args])
#         x = func(*newargs)
#         print('end decorator22')

#         return x

#     return wrapper

# def decorator2(func):
#     print('decorator2')
#     def wrapper(*args):
#         print('start decorator2')

#         if args is not None:
#             newargs = tuple([x+1 for x in args])
#         x = func(*newargs)
#         print('end decorator2')

#         return x
#     return wrapper


# # if decoraotr no args, default one argment => function name

# @decorator22
# @decorator2
# def test2(*args):
#     print('test2')
#     print(args)
    
# test2(23)

# # test2 = decorator22(decorator2(test2))

# l = [23,4,16,4,23,1,74,235,23,1,524,2,524,16,4,3]
# # 方法一
# # new_l = []
# # for i in l:
# #     if i not in new_l:
# #         new_l.append(i)

# # 方法二

# new_l = sorted(set(l), key=l.index)

# # func = lambda x,y : x 
# def func(x,y):
#     if y in x:
#         # print('y in x:',x)
#         return x
#     else:
#         print('y not in x:',x+[y])
#         return x + [y]

# print(reduce(func, [[],]+l))



# import random
# def find_sec_max(num_list):
#     if len(num_list) < 2:
#         return num_list[0]
#     max_num = num_list[0]
#     sec_max_num = num_list[1]
    
#     for num in num_list:
#         if num > max_num:
#             sec_max_num = max_num
#             max_num = num
            
#         elif num > sec_max_num:
#             sec_max_num = num
#     return sec_max_num

# nums = random.sample(range(100),10)
# result = reduce(lambda x,y: max(x,y) ,nums)
# print(nums)
# print(result)
# print('find_sec_max,', find_sec_max(nums))

# import re

# pattern = r'(([0-1]?\d{1,2}|2[0-5][0-5])\.){3}([0-1]?\d{1,2}|2[0-5][0-5])'

# print(re.search(pattern, '1123.24.52.12'))

import sys

from shiboken6 import Object

# Getting size using getsizeof() method and lately
# printing the same.


# init size of list defined
# list_result = []
# for i in range(101):
#     test_list = [str(x) for x in range(i)]
#     list_result.append(sys.getsizeof(test_list))


l = []
for i in range(101):
    r = [j for j in range(i)]
    l.append((i,sys.getsizeof(r)))

print(l)
list_4 = [str(x) for x in range(24)]
print('before append allocated bytes:',sys.getsizeof(list_4))
list_4.append('jkh')
print('after append allocated bytes:',sys.getsizeof(list_4))


def count_newallocate(orgsize, new_size):
    # new_size: 新分配的对象数量
    # 
    new_allocated = (new_size + (new_size >> 3) + 6 ) & ~3
    if (new_size - orgsize) > (new_allocated - new_size):
        new_allocated  = (new_size + 3) & ~3
    print(f'{new_allocated=}')
    print(f'list_resize bytes: {new_allocated*8+56}')
    
count_newallocate(len(list_4),len(list_4)+1)
