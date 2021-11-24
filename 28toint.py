# 字符串'123' 转换 123 不使用int()

# 方法一 ord
def toint(s):
    # ord 将字符转换成ASCII 数值
    # 从个位开始遍历（从字符串顺序遍历）
    # 1 -> 1 + 0
    # 12 - > 1 * 10 + 2
    # 123 -> 12 * 10 + 3
    # ....
    num = 0
    for c in s:
        num = num * 10 + ord(c) - ord('0')
    return num 

# 方法二 str

def toint_str(s):
    num = 0
    for c in s:
        for i in range(10):
            if str(i) == c:
                num = num * 10 + i





print(toint('4891'))