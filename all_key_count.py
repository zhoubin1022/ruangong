import re
from keyWord import keyWord


def all_key(word):
    count = 0
    for line in word:
        words = re.split(r'[^a-zA-Z]', line)
        for x in words:
            if x:
                for key in keyWord:
                    if key == x:
                        count += 1
                        break
    print("total num: ", count)

