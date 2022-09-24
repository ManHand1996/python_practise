from threading import Thread
from multiprocessing.pool import ThreadPool
from multiprocessing import Lock
import time

total = 20000000
def read(n,l):
    global total
   
    for i in range(1000000):
        total -= 1
    #time.sleep(1)
    l.acquire()
    try:
        
        print('reading data...',n)
    finally:
        l.release()
    
def write(n,l):
    
    # do something about this threading...
    l.acquire()
    try:
        global total
        for i in range(1000000):
            total -= 1
        # using some share device or data must be use LOCK!
        print('writing data..',n)
    finally:
        l.release()
    
    #time.sleep(0.5)

l = Lock()
threadpool = ThreadPool()
for i in range(10):
    if i % 2== 0:
        threadpool.apply_async(func=write, args=(i,l))
    else:
        threadpool.apply_async(func=read, args=(i,l))

threadpool.close()
threadpool.join()
print(total)