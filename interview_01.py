"""
Python 变量，对象，引用
"""
# a 是变量， 是一个指向对象内存空间的指针，这个关系就叫引用
# 与C语言不同的是，Python使用的是引用语义，C语言使用值语义

# 简单理解
# 值语义：当复制这个对象时，会开辟新的内存空间，使复制对象与原对象无关
# 引用语义（指针）：将新的变量指向被复制对象的内存空间中，引用计数+1

# a = 100
import sys
from ctypes import c_long
import gc

gc.disable()
# gc.disable()
# a = [1]
# b = [2]
# a.append(b)
# b.append(a)
# a_id = id(a)
# b_id = id(b)
# print('a id:', hex(a_id))
# print('b id:', hex(b_id))
# print('b:',c_long.from_address(a_id).value)
# print('a:',c_long.from_address(b_id).value)

# print('b[1]:',c_long.from_address(id(b[1])).value)
# print('a[1]:',c_long.from_address(id(a[1])).value)

# del b
# del a

# print('after del a,b')

# print('a ref_cnt:',c_long.from_address(a_id).value)
# print('b ref_cnt:',c_long.from_address(b_id).value)
# print('garbage list: ',gc.garbage)
# gc.set_debug(gc.DEBUG_COLLECTABLE)
# # gc.collect(0)



# print('after gc:')
# print('a ref_cnt:',c_long.from_address(a_id).value)
# print('b ref_cnt:',c_long.from_address(b_id).value)

# class MyBadClass:
#   def __init__(self, name):
#     self.name = name

#   def __del__(self):
#     global person # create an externally accessible pointer...
#     person = self # ... and point it at the object about to be removed
#     print(f'deleting {self.name}!')

# jane = MyBadClass('Jane')
# bob = MyBadClass('Bob')
# jane.friend = bob
# bob.friend = jane

# print(gc.get_referents(jane))
# del jane
# del bob

import sys
cart = []
class PlagueVictim:
    RETORTS = ("I'm not dead.",
               "I'm getting better.",
               'I feel fine.',
               "I think I'll go for a walk.",
               'I feel happy. I feel happy.')
    DEFAULT_RETORT = "I'm still not dead."
    @classmethod
    def retort(cls, i):
        try: return cls.RETORTS[i]
        except IndexError: return cls.DEFAULT_RETORT
    def __init__(self): self.incarnation = 0
    def __del__(self):
        print(self.retort(self.incarnation))
        if cart is not None: cart.append(self)
        self.incarnation += 1

cart.append(PlagueVictim())
print("> Here's one.")
print(len(cart))
cart.pop() and None
if not cart: sys.exit()

print(">> 'ere, he says he's not dead.")
# Stubborn, aren't you?
cart.pop() and None
del PlagueVictim.__del__
print('*thwack*')
# cart.pop() and None
print('>> Ah, thank you very much.')
print(len(cart))