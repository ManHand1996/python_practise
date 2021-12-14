
from functools import wraps
import datetime
# def DecoratorTime(f1):
#     print(f1)
#     @wraps
#     def wrapper(func,*args, **kwargs):
#         print(args)
#         print(kwargs)
#         if datetime.datetime.now().day >= 5:
#             print('END1...')
#             return func(*args, **kwargs)

#         else:
#             print('END2...')
#             raise BaseException('aaaa')
        
#     return wrapper


# @DecoratorTime(f1=2442)
# def test(*args,**kwargs):
#     print('test:')
#     print(args)
#     print(kwargs)




# 1.装饰器带参数
# 相当于 test2 = d2(f=12)(test2)
def d2(f=0):
    print(f)

    # def wrapper(func):
    #     print('装饰器带参数')
    #     def deco( *args, **kwargs):
    #         func(*args)
    #     return deco
    
    def wrapper(func, *args, **kwargs):
        func(*args, **kwargs)
        # test2 =  wrapper(test) -> None
        # test2()
    return wrapper

@d2(f=12)
def test2(*args):
    
    print('test2')
    print(args)
# wrapper = deco
# test2 = wrapper(test) -> deco 可调用对象
# test2 = test2(1,11)

# 2.被装饰器函数带参数

# def d3(func):
#     def wrapper(*args, **kwargs):
#         print('被装饰器函数带参数 start')
#         r = func(*args, **kwargs)
#         print('被装饰器函数带参数 end')
#         return r
#     return wrapper

# @d3
# def test3(*args, **kwargs):
#     print('test3')

# test3(1,2,3,a=123)

# test2 = 

# def get_parameter(*args,**kwargs):  # 工厂函数，用来接受@get_parameter('index.html/')的'index.html/'
#     def log_time(func):
#         def make_decorater():
#             print(args,kwargs)
#             print('现在开始装饰')
#             func()
#             print('现在结束装饰')
#         return make_decorater
#     return log_time

# @get_parameter('index.html/')
# def test2():
#     print('我是被装饰的函数')
    # return num+1

# 2.被装饰函数带参数

# 3.两者都带参数



#问题1.装饰器在定义时已经运行?
# 是的，相当于  
# test = wrapper(test)
