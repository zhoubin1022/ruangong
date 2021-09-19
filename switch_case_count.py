import all_key_count


def sc_count(word):
    switch_count = 0
    case_count = []
    all_word = all_key_count.all_key(word)

    for words in all_word:
        for x in words:
            if x == 'switch':
                switch_count += 1
                case_count.append(0)
            elif x == 'case':
                case_count[switch_count-1] += 1
    print("switch num: ", switch_count)
    print("case num: ", end=' ')
    for i in case_count:
        print(i, end=' ')
    print()
    return all_word

