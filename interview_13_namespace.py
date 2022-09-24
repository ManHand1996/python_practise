"""
namespace:
是指Python的所有对象（可以是变量和函数）都有一个独一无二的名称
"""
# import interview_09_logging
# interview_09_logging.log_with_dict()
# print('locals:', locals())

# global scope
var1 = 10
from sys import path
def func():
    # local scope
    var2 = 20
    def func2():
        # nested scope
        var3 = 30
        print(var2)
    

print('locals:', globals())