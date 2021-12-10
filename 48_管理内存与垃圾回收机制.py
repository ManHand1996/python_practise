'''
https://www.jb51.net/article/161474.htm
Python 内存管理机制：
1.引用计数
    高效内存管理手段
    python中的对象被引用时，引用计数+1, 当引用计数为0时，删除对象

2.垃圾回收
    a.引用计数
    b.标记清除（针对容器循环引用）
        两个容器指针和容器对象，便于追踪对象引用
        跟进两个链进行清除（root chain, unreachable chain）

    c.分代回收
        

        Python 跟进阈值进行垃圾对象回收
        分代回收分三个级别，数字越大表示存活越久，对应的阈值也不一样
        G0, 新建对象  threshold0 < 对象创建数 - 对象释放数
        G1, G0回收存活 threshold1 < G0回收次数
        G2, G1回收存活  threshold2 < G1回收次数
        
3.内存池
三层：
0：C malloc , free
1：PyMem_Malloc < 256k 由该层分配
2：对python对象操作
'''

