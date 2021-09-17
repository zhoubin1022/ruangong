import switch_case_count


def elif_count(word, flag):
    if_else_num = 0  # 所有if else 的个数
    elif_num = 0  # 所有if else if else 的个数
    if_pos = []  # 所有if 的位置
    if_num = 0     # 所有if 的个数
    all_str = []  # 所有if， else， else if的集合
    all_num = 0  # 所有if， else， else if的个数
    # if == 1, else == 2, else if == 3
    all_word = switch_case_count.sc_count(word)
    # print(all_word)
    for line in all_word:
        # print(line)
        len_line = len(line)
        for i in range(len_line):
            if line[i] == 'if':
                if_num += 1
                if_pos.append(all_num)
                all_str.append(1)
                all_num += 1
            elif line[i] == 'else':
                if i < len_line-1 and line[i+1] == 'if':
                    all_str.append(3)
                    all_num += 1
                else:
                    if_num -= 1
                    str_len = all_num - if_pos[if_num-1] - 1
                    all_num = if_pos[if_num-1] + 1
                    all_str = all_str[0: all_num]
                    if_pos = if_pos[0: -1]
                    '''all_num = if_pos[if_num-1]
                    all_str = all_str[0:if_num]
                    
                    if_pos = if_pos[0:-2]
                    '''
                    if str_len == 2:
                        if_else_num += 1
                    else:
                        elif_num += 1
        # print(all_str)
    print("if-else num: ", if_else_num)
    if flag == 4:
        print("if-elseif-else num: ", elif_num)
