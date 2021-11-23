
# 根据指定路径，找出目标文件路径
# / -> *.pyc
import os
def findFilePath(root_path, suffix):

    if os.path.isfile(root_path):
        if (root_path.find(suffix) >= 0):
            print(root_path)
    else:
        for new_path in os.listdir(root_path):
            findFilePath(os.path.join(root_path, new_path),suffix)


findFilePath("D:\\Download\\django_analysis",".pyc")
