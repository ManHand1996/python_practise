
"""
装饰器理解:

1.装饰器返回的是可调用对象
2.装饰器定义时已经运行
3.装饰器实际是对函数进行重新定义
格式:

func_name = (decorator(params))(func_name) # 带参数
func_name = decorator(func_name) # 无参数

# 多个装饰器

func_name = dec1(params)(dec2(params)(func_name)) # 定义时从inside装饰器开始执行, 定义是只是执行该装饰器函数

func_name() # 调用时,从outdis开始指向, 即装饰器的内部函数





"""

import datetime


def decorator_no_parmas(func):
    
    print('decorator_no_parmas',func.__name__)
    def wrapper(*args, **kwargs):
        print('start decorator_no_parmas')
        
        func(*args, **kwargs)
        print('end decorator_no_parmas')

         
    return wrapper


def decorator_parmas(g=3):
    # 装饰器返回可调用对象 , 解释时会将原函数对象作为第一个参数 obj(func_name)
    def decorator(func):
        print('decorator_parmas',func.__name__)
        # 原函数参数
        def wrapper(*args, **kwargs):
            print('start decorator_parmas')
            func(*args, **kwargs)
            print('end decorator_parmas')
            
        return wrapper
        # return func(*args, **kwargs)

    return decorator


# @decorator_no_parmas
# @decorator_parmas(g=5)
def test2(a, b):
        
    print(a + b)



test2 = decorator_no_parmas(decorator_parmas(g=4)(test2))

test2(10,20)

print(test2.__name__)

