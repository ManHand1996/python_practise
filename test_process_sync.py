from multiprocessing import Lock, Process
def f(l, i):
    '''
    由于print属于IO系统调度， 系统的共享资源
    要正确输出到控制台
    需要确保每个进程里的每次使用的IO时，其他进程不会占用
    否则会导致多个进程输出内容的重叠在一起：
    因为print是阻塞的，所以内核缓冲区会一直接收数据，直到应用层发送完毕。所以输出时可能多个进程会同时写入到内核缓冲区。输出到控制台

    '''
    # print('hello world', i)
    
    # 不加锁会输出：hello worldhello world  76
    # 加上会正常或者进程使用join（阻塞）等待上一个进程完成
    
    # l.acquire()
    # try:
    print('hello world', i)
    # finally:
    #     l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        p1 = Process(target=f, args=(lock, num))
        p1.start()
        # 添加join可以避免IO调用竞争（如print）
        
        # p1.join()
