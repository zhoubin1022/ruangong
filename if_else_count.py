import re

import keyWord
import switch_case_count


def elif_count(word, flag):
    all_word = switch_case_count.sc_count(word)
    new_word = keyWord.saveKey(all_word, ['if', 'else', '{', '}'])
    # 存放结果
    if_else_num = 0  # 所有if else 的个数
    elif_num = 0  # 所有if else if else 的个数

    key_stack = []  # 堆栈
    # if_left = []  # if结构里面左括号数量
    left_pos = []  # 所有左括号在堆栈的位置
    '''
    if_num = 0     # 所有if 的个数
    all_str = []  # 所有if， else， else if的集合
    all_num = 0  # 所有if， else， else if的个数
    '''
    # if = 1, else = 2, else-if =3, '{' = 4, '}' = 5.
    for line in new_word:
        len_line = len(line)
        i = 0
        while i < len_line:
            if line[i] == 'if':
                key_stack.append(1)
            elif line[i] == '{':
                left_pos.append(len(key_stack))
                key_stack.append(4)
            elif line[i] == 'else':
                if i < len_line - 1 and line[i + 1] == 'if':  # else-if 结构
                    key_stack.append(3)
                    i += 1  # 跳过if
                else:
                    key_stack.append(2)
            elif line[i] == '}':
                temp = key_stack[left_pos[-1]+1:]
                key_stack = key_stack[:left_pos[-1]]
                left_pos.pop()
                for t in range(len(temp)):
                    temp[t] = str(temp[t])
                str_tmp = ''.join(temp)
                # print(temp, key_stack)
                pat_1 = re.compile(r'12')
                pat_2 = re.compile(r'13+2')
                if_else_num += len(pat_1.findall(str_tmp))
                elif_num += len(pat_2.findall(str_tmp))
            i += 1
            # print(key_stack)
    # print(all_word)
    '''for line in all_word:
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
                    # all_num = if_pos[if_num-1]
                    # all_str = all_str[0:if_num]
                    # if_pos = if_pos[0:-2]
                    if str_len == 2:
                        if_else_num += 1
                    else:
                        elif_num += 1
        # print(all_str)
'''
    print("if-else num: ", if_else_num)
    if flag == 4:
        print("if-elseif-else num: ", elif_num)