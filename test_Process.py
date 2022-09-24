#from multiprocessing import process
from multiprocessing import Process
from time import sleep, strftime, localtime
import os
import datetime
print('当前进程：',os.getpid())

def work1(*args):
    print(args)
    print(args[0])

def work2(sleeptime):
    print(strftime('%Y-%m-%d %H:%M:%S', localtime()))
    sleep(sleeptime)

def work3(sleeptime):
    print(strftime('%Y-%m-%d %H:%M:%S', localtime()))
    sleep(sleeptime)



class MyProcess(Process):

    def __init__(self, *args):
        # super().__init__()
        Process.__init__(self)
        self._args = args
        self.runtime = 5
        self.daemon = True # 守护进程，当主进程完结时，尝试终止子进程
       
    def run(self):

        sleeptime = self._args[0]
        while self.runtime > 0:
            print(self.name,'正在运行：',self.runtime,'第{0}次'.format(5-self.runtime),self.pid)
            print(strftime('%Y-%m-%d %H:%M:%S', localtime()))
            sleep(sleeptime)
            self.runtime -= 1

if __name__ == '__main__':

    for i in range(10):
        p1 = MyProcess(1)

        p1.start()

        p1.join()
        # p1.close() # 主动释放资源


'''
Process.close() : 进程结束时主动回收资源（并不一定马上进行）
Process.kill() : 终止进程给进程发送SIGKILL信号 参考命令行 kill -9
Process.terminal(): 杀死进程，最好避免对使用共享资源的进程使用
有可能发生如下情况：
1.进程马上退出
2.进程退出并过一段时间后回收资源
3.进程一直运行

所以在join,kill,terminal后需要执行close确保进程占用的资源会回收

参考链接：
https://major.io/2010/03/18/sigterm-vs-sigkill/
https://stackoverflow.com/questions/58866837/python3-multiprocessing-terminate-vs-kill-vs-close

'''

