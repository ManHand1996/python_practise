
'''
进程池使用

'''

from multiprocessing import Pool,get_context

def f(x):
    return x * 2

pool = Pool(processes=5)
# 异步执行 非阻塞式
# 返回AscyncResult对象
result_sync = pool.apply(f, args=(3,))

result = pool.apply_async(f, args=(1,))

print(result_sync)
print(result.get(1))

if result.ready():
    # 映射 阻塞式
    result3 = pool.imap(f, range(5))
    print(next(result3))
    print(result3.next(timeout=0.000000000000000000000001))
    result2 = pool.map(f, range(5))
    print(result2)
pool.close() # 停止添加进程
pool.join() # 阻塞主进程，知道进程池的进程执行完。


print('hello ')

