'''
python中没有接口类但可以通过继承变相实现
接口类实现（抽象类的一种，本质是继承方法并实现）

1.预定义一系列方法但不实现
2.接口类不能实例化
3.推荐多继承，越多越好
4.归一化（不关心实现，对所有拥有该接口的对象都作统一处理）

接口类概念：
1.接口类是抽象类的变种
2.接口类的所有方法都是抽象的
3.接口类的变量都是静态的
4.多继承
'''

# 接口类实现 方法1.
# class Payment:
#     def pay(self, money):
#         raise NotImplementedError    #手动抛异常


# class Alipay(Payment):
#     def paying(self, money):  # 这里类的方法不是一致的pay,导致后面调用的时候找不到pay
#         print('支付宝支付了')

# def pay(payment, money):  # 支付函数，总体负责支付，对应支付的对象和要支付的金额
#     payment.pay(money)

# p = Alipay()  # 不报错
# pay(p, 200)  #调用的时候才会报错  'Alipay' object has no attribute 'pay'


# 接口类实现 方法2 推荐

# 若实现类，没有实现接口类则在初始化时会报错
# 并且接口类Payment 不能实例化
from abc import ABCMeta,abstractmethod
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

class Alipay(Payment):
    def pay(self, money):
        print('Alipay payed')

# 归一化
def pay(payobj, money):
    payobj.pay(money)


p = Alipay() 
pp = Payment()
pay(p,2)
pay(pp,2)






