# 在这个文件中，我将会执行读入文件，并根据输入调用对应的函数的操作
# 读入文件路径和完成等级
# 程序入口
# from keyWord import keyWord


# 用来标记之前有没有/*，即接下来是不是注释部分，1表示是注释，0表示不是注释

import all_key_count
import if_else_count
import switch_case_count

flag = 0


# 遇到{}在前后添加空格
def addBlank(word_list):
    return word_list.replace('{', " { ").replace('}', " } ")


def judge(word_list):  # 删去每一行注释的函数，
    word_list = addBlank(word_list)
    global flag
    len_list = len(word_list)
    if flag == 0:  # 这部分不是注释内部
        for x in range(len_list):
            if word_list[x] == '/':
                if x < len_list - 1:
                    if word_list[x + 1] == '/':
                        return word_list[0: x]

                    elif word_list[x + 1] == '*':
                        flag = 1
                        return word_list[0: x]
        return word_list
    else:
        for x in range(len_list):
            if word_list[x] == '*':
                if x < len_list - 1 and word_list[x + 1] == '/':
                    flag = 0
                    if x == len_list - 2:
                        return
                    else:
                        return word_list[x + 2: -1]
        return


if __name__ == "__main__":
    path = input("输入文件路径：")

    completeLevel = int(input("输入完成等级："))
    # 判断输入的等级是否不在范围内
    while completeLevel <= 0 or completeLevel > 4:
        completeLevel = int(input("输入错误，请再次输入完成等级："))
    word = []
    try:  # 打开文件并读文件
        with open(r''+path, 'r', encoding="utf-8") as file:
            for list1 in file:
                list1 = list1.replace('\n', '').strip()
                list1 = judge(list1)
                if list1:
                    word.append(list1)
    except IOError:
        print("Error: 没有找到文件或读取文件失败")
    else:  # 根据等级进行操作
        if completeLevel == 1:
            all_key_count.all_key(word)
        elif completeLevel == 2:
            switch_case_count.sc_count(word)
        else:
            if_else_count.elif_count(word, completeLevel)
