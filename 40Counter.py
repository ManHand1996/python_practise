# 统计一段字符串中字符出现的次数



from collections import Counter

import pympler
def CounterStr(letter_str):
    c = {}
    for s in letter_str:
        if s not in c.keys():
            c[s] = 1
        else:
            c[s] += 1
    
    return dict(sorted(c.items(), 
                       key = lambda x:x[1], 
                       reverse=True))


def CounterStr2(letter_str):
    return ",".join(map(lambda x: x[0] +':'+ str(x[1]), Counter(letter_str).most_common()))
    return Counter(letter_str).most_common(5)

print(CounterStr('abffa23ggglll'))
print(CounterStr2('abffa23ggglll'))
