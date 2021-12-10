
from functools import wraps
import datetime
def DecoratorTime(*args, **kwargs):

    def wrapper(func):
        print(args)
        print(kwargs)
        if datetime.datetime.now().day >= 5:
            print('END1...')
            return func

        else:
            print('END2...')
            raise BaseException('aaaa')
        
    return wrapper


@DecoratorTime(1,2,3,a=1,b=2,c=3)
def test(*args,**kwargs):
    print('test:')
    print(args)
    print(kwargs)

#问题1.装饰器在定义时已经运行?
# 是的，相当于  
# test = wrapper(test)

#test('lllllli',kw=123,ll=123)