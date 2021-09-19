import all_key_count
import keyWord


def sc_count(word):
    # 最后存储的结果
    switch_count = 0
    case_count = []

    key_stack = []  # 堆栈
    switch_pos = []  # 堆栈执行过程中switch在堆栈中的位置
    switch_left = []  # switch结构中左括号的数量
    out_left = 0  # switch外左括号数量
    all_word = all_key_count.all_key(word)
    new_word = keyWord.saveKey(all_word, ['switch', 'case', '{', '}'])
    # switch = 1, case = 2, { = 3, } = 4.
    '''for line in new_word:
        print(line)'''
    for line in new_word:
        for x in line:
            if x == '{':
                if not switch_pos:  # 属于外括号
                    out_left += 1
                else:  # 属于内括号
                    key_stack.append(3)  # 加入堆栈
                    switch_left[-1] += 1  # 对应左括号加1
            elif x == 'switch':
                key_stack.append(1)
                switch_pos.append(len(key_stack))
                switch_left.append(0)
                case_count.append(0)
                switch_count += 1
            elif x == 'case':
                case_count[switch_count-1] += 1
            elif x == '}':
                if not switch_pos:  # 属于外括号
                    out_left -= 1
                else:  # 属于内括号
                    switch_left[-1] -= 1  # 对应左括号-1
                    if switch_left[-1] == 0:  # 当前switch结束
                        key_stack = key_stack[0:switch_pos[-1]]  # 出栈
                        switch_pos.pop()

    '''for words in all_word:
        for x in words:
            if x == 'switch':
                switch_count += 1
                case_count.append(0)
            elif x == 'case':
                case_count[switch_count-1] += 1'''
    print("switch num: ", switch_count)
    print("case num: ", end=' ')
    for i in case_count:
        print(i, end=' ')
    print()
    return all_word

