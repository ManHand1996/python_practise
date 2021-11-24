
# 根据指定路径，找出目标文件路径
# / -> *.pyc
import os
# 方法一递归
def findFilePath(root_path, suffix):

    if os.path.isfile(root_path):
        if (root_path.find(suffix) >= 0):
            print(root_path)
    else:
        for new_path in os.listdir(root_path):
            findFilePath(os.path.join(root_path, new_path),suffix)

# 方法二 os.walk(top[, topdown=true[,onerrorNone[,followlinks=false]]]) ->
# 创建生成器generator， 用于查找目录和子目录下的所有文件
# arg: topdown = true 自上而下(即从当前路径开始往下查找所有文件) 反之亦然
# 返回3元组（path:str, path_name:[], file_name:[]）

def findFileWithWalk(root_path, suffix):
    for path,path_names, filenames in os.walk(top=root_path):
        for filename in filenames:
            # if filename.find(suffix) >= 0:
            #     print(os.path.join(path,filename))
            # name,suf =os.path.splitext(filename)
            # if suf == suffix:
            #     print(os.path.join(path,filename))
            if filename.endswith(suffix):
                print(os.path.join(path,filename))

# 方法三 glob

from glob import iglob
def glob_func(fp, postfix):
    for i in iglob(f"{fp}/**/*{postfix}",recursive=True):
        print(i)

#findFilePath("D:\\Download\\django_analysis",".pyc")

#findFileWithWalk("D:\\Download\\django_analysis",".pyc")
glob_func("D:\\Download\\django_analysis",".pyc")