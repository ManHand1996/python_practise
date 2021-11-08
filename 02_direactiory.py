#-*-coding:utf-8 -*-
# def print_directory_contents(sPath): 
#     """ 
#     这个函数接收文件夹的名称作为输入参数 
#     返回该文件夹中文件的路径 
#     以及其包含文件夹中文件的路径 
#     """
#     pass

import os
def print_directory_contents(sPath):
    # 先判断是否路径
    # 是：获取文件夹下的子文件/文件夹，递归print_directory_contents(path)
    # 否：退出 输出文件名
    if os.path.isdir(sPath):
        print(os.path.abspath(sPath))
        # print(os.path.dirname(os.path.abspath(sPath)))
        for subpath in os.listdir(sPath):
            print_directory_contents(os.path.join(sPath,subpath))
    else:
        print(sPath)
print("start...............................")
print_directory_contents("E:\BaiduNetdiskDownload")