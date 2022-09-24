import re
s1 = 'That she is a rich woman is known to us all. This party is very good. We don\'t know that you had sold your phone.\n Do your wanna this apple?'

#s1 = 'That she is a rich woman is known to us all. We didn’t know (that) you had sold your house. This party is very good. Do you wanna this apple? No, thanks.'
# 反向先行
pstr = r'[^.\!\?\n\r]*(?!that)*this[^.\!\?\n\r]*(?!that)*.'

# 反向后行
pstr2 = r'(?<!that)*[^.\!\?\n\r]*this(?<!that)*[^.\!\?\n\r]*.'
pattern1 = re.compile(pstr2,re.M|re.I)
result = re.findall(pattern1, s1)
if result:
    print(result)