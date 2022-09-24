"""


协程：比线程更高效（没有切换线程的开销，没有锁）
多进程+协程


应用：
生产者-消费者模式

一般使用多线程实现，但多线程有锁，容易会出现死锁问题。
使用协程实现更高效
"""

import greenlet
import asyncio

from sqlalchemy import true

def custom():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('custom doing..{}'.format(n))
        r = 'OK'




def produce(custom):
    custom.send(None)
    n = 0
    while n < 10:
        n += 1
        print('produce doing.. {}'.format(n))
        r = custom.send(n)
        # print('custom return: num-{},{}'.format(n,r))
        print(f'custom return: num-{n},{r}')
        


async def wget(host):
    print('wget %s' % host)
    connect = asyncio.open_connection(host, 80)
    reader,writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('{} header -> {} '.format(host, line.decode('utf-8')))
    writer.close()
    

async def hello_asyncio():
    print('hello')
    await asyncio.sleep(1)
    print(' asyncio..')

if __name__ == '__main__':
    foo = '''asfasfasf
asfasf
asfasf'''
    
    print(repr(foo))
    # loop = asyncio.get_event_loop()
    # tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    # tasks.append(hello_asyncio())
    # loop.run_until_complete(asyncio.wait(tasks))