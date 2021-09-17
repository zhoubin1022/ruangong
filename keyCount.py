# 在这个文件中，我将会执行读入文件，并根据输入调用对应的函数的操作
# 读入文件路径和完成等级
# 1.消去注释
# from keyWord import keyWord


# 用来标记之前有没有/*，即接下来是不是注释部分，1表示是注释，0表示不是注释
flag = 0


def judge(word_list):   # 删去每一行注释的函数
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
    while completeLevel <= 0 or completeLevel > 4:
        completeLevel = int(input("输入错误，请再次输入完成等级："))
    word = []
    with open(path, 'r', encoding="utf-8") as file:
        for list1 in file:
            list1 = list1.replace('\n', '').strip()
            list1 = judge(list1)
            if list1:
                word.append(list1)
    if completeLevel == 1:
        print(1)
    elif completeLevel == 2:
        print(2)
    elif completeLevel == 3:
        print(3)
    elif completeLevel == 4:
        print(4)
    '''for i in word:
        print(i)'''