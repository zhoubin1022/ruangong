import re
from keyWord import keyWord


def all_key(word):
    count = 0
    all_word = []
    for line in word:
        words = re.split(r'[^a-zA-Z0-9_{}]', line)  # 使用正则表达式分割字符串
        words = [item for item in filter(lambda t:t != '', words)]  # 删去空字符串
        if not words:  # 计数
            continue
        all_word.append(words)
        for x in words:
            if x:
                for key in keyWord:
                    if key == x:
                        count += 1
                        break
    # print(all_word)
    print("total num: ", count)
    return all_word
