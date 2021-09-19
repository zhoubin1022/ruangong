import re
from keyWord import keyWord


def all_key(word):
    count = 0
    all_word = []
    for line in word:
        words = re.split(r'[^a-zA-Z0-9_{}]', line)
        words = [item for item in filter(lambda t:t != '', words)]
        if not words:
            continue
        all_word.append(words)
        for x in words:
            if x:
                for key in keyWord:
                    if key == x:
                        count += 1
                        break
    print(all_word)
    print("total num: ", count)
    return all_word

