# 8.将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}


s = "k:1 |k1:2|k2:3|k3:4"

# 列表生成式
d = [ (k,int(v)) for sub in s.split("|") for k,v in (sub.split(':'),) ]
print(dict(d))
# 字典推导式
d1 = {k:int(v) for t in s.split("|") for k,v in (t.split(":"),)}
print(d1)


alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]

new_alist = sorted(alist, key = lambda x : -x['age'])
print(new_alist)