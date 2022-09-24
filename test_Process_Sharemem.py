from multiprocessing import Array,Value, Process
from ctypes import py_object
# Array -> 共享内存的列表
# Value -> 共享内存的对象

# 这些共享对象将是进程和线程安全的。

class MyObject:
    
    def __init__(self) -> None:
        self.__value = 0

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val

def changeVal(obj,val, ps_name):
  
    obj.value = val
    print(ps_name,': share object value is ',obj.value)

if __name__ == '__main__':
    myobj = MyObject()
    
    
    # 将目标对象进行deep copy
    share_obj = Value(py_object, myobj)
    p1 = Process(target=changeVal, args=(share_obj, 10, 'p1'))
    p2 = Process(target=changeVal, args=(share_obj, 100, 'p2'))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(myobj.value)
    # print(hex(id(share_obj)))
    # print(hex(id(myobj)))
