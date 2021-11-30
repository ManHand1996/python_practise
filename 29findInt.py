l1 = [2,7,11,15]
target = 17
# result = []
# for i in l1:
#     fl =list(filter(lambda x: (target-i) in l1, l1))
#     if len(fl) > 0:
#         result.append(l1.index(i))
#         result.append(l1.index(target-i))
#         break

result = list(filter(lambda x: (target-x) in l1, l1))
idx_list = []
if len(result) >= 2:
    result = result[:2]
    idx_list = list(map(lambda x:l1.index(x), result))

print(idx_list)

