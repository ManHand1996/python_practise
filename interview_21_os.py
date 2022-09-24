from functools import reduce
import os


def os_rename():
    
    # os.path 与文件路径相关的模块
    # os.rename('./testn.log','./test.log')
    abs_path = os.path.abspath('.')
    new_path = os.path.join(abs_path, 'test_fd')
    # os.mkdir(new_path)

    # os.open 只能是文件才能创建，打开路径 的文件描述符需要, os.O_RDONLY
    dst_d_fd = os.open('./test_fd', os.O_RDONLY)
    src_d_fd = os.open('./', os.O_RDONLY)

    print(f'dst dir fd: {dst_d_fd} \n src dir fd: {src_d_fd}')

    # os.rename， 如果使用文件描述符操作，src和dst需要绝对路径 
    # os.rename(src=os.path.join(abs_path, 'test.log'),
    #           dst=os.path.join(new_path, 'testn.log'),
    #           src_dir_fd=src_d_fd, 
    #           dst_dir_fd=dst_d_fd)

    os.rename(src='./test.log',
            dst='./test_fd/test.log')

    os.close(dst_d_fd)
    os.close(src_d_fd)


def os_remove():
    os.remove('./test.log')
    

def os_walk(root_path):
    # os.walk(top=, topdown=True)
     
    exclude_path = ['logpack', '.git']
    for dirpath, dirnames, filenames in os.walk(top=root_path):
        print(dirpath, dirnames, filenames)
        if exclude_path:
            for expath in exclude_path:
                dirnames.remove(expath)
            exclude_path = None
        

def os_mkdir():
    # mode:权限模式 用8进制表示 0o
    os.mkdir('./hellworld')
    # os.makedirs(name='./hellworld/foo', mode=0o777, exist_ok=True)
    

def os_chmod():
    import stat
    os.chmod('./hellworld', mode=stat.S_IRWXU|stat.S_IXGRP|stat.S_ISUID|stat.S_ISGID)
if __name__ == '__main__':
    # os_walk('./')
    os_chmod()