
'''
python 进程间通信:
1.Queue 队列

2.Pipe 管道（默认双工）
尽量避免对使用共享资源的进程执行terminate(Process和Pool对象一样情况)

'''
from multiprocessing import Pool, Queue, Pipe
import multiprocessing
from multiprocessing.connection import Connection
from pickle import NONE
import random, time

def fun(conn: Connection, i):
   
    print('pipe send')
    if i % 2 == 0:
        for i in range(10):
            data = random.randint(1,100)
            print('process ',i, ' send', data)
            
            conn.send({'data':data, 'status':'SEND'})
            time.sleep(0.5)
        conn.send({'data':None, 'status':'END'})

def funrecv(conn: Connection,i):
    if i % 2 != 0:
        
        result = None
        while True:
            result = dict(conn.recv())
            if not result['data']:
                break
            print('recv :',result['data'])
        # if result['status'] != 'END':
        #     print(result['data'])
        # while conn.poll() or result['status'] != 'END':
        #     print('process ',i, ' recv')
        #     result = conn.recv()
        #     print(result['data'])





if __name__ == '__main__':
    # 队列通信，存储共享变量
    # 队列是线程和进程安全的。


    parent_pipe , child_pipe = Pipe()
    pool = Pool(5)
   
    pool.apply_async(fun, args=(child_pipe, 0))
    pool.apply_async(funrecv, args=(parent_pipe, 1))

    # 一般同时执行
    pool.close()
    pool.join()
    # 获取创建进程的上下文（根据系统不同），windows： spanw; unix: spawn,fork ------ 启动进程的方法
    # ctx = multiprocessing.get_context('fork')
    # print(ctx.__str__)