# 统计一个文本中单词频次最高的10个单词？

import re
def solution(filepath):
    # 1. 按行读取文件
    # 2. 提取每行中的单词（过滤空格，逗号句号等不必要字符）
    # 3. 将单词放到字典中统计
    count_words = {}
    
    with open(filepath) as f:
        for line in f.readlines():
            
            result_line = re.findall(r'\w+', line)
            for word in result_line:
                if word in count_words.keys():
                    count_words[word] += 1
                else:
                    count_words[word] = 1
    return_word = sorted(count_words.items(), key=lambda x: x[1], reverse=True)[:10]
    return_word = [wd[0] for wd in return_word]
    return return_word

# def test(filepath):
#     distone = {}
#     with open(filepath) as f:
#         for line in f:
#             print(line)
#             # \W 匹配非字母数字和下划线
#             line = re.sub("\W+", " ", line)
            
#             lineone = line.split()
#             for keyone in lineone:
#                 if not distone.get(keyone):
#                     distone[keyone] = 1
#                 else:
#                     distone[keyone] += 1
#     num_ten = sorted(distone.items(), key=lambda x:x[1], reverse=True)[:10]
#     num_ten =[x[0] for x in num_ten]

#     return num_ten

# 方法2
from collections import Counter 
def solution2(word_path):
    result_list = []
    with open(word_path) as f:
        # 使用内置统计 
        # Counter.most_common(num:int) -> [(str,int)]

        
        result_list = list(map(lambda x:x[0], Counter(re.sub('\W+' ," ",f.read()).split()).most_common(10)))
    return result_list

word_path = 'D:\\testcount.txt'

word_count = solution(word_path)
word_count2 = solution2(word_path)
print(word_count)
print(word_count2)
