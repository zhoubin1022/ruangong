# 列出要查找的关键字
keyWord = [
    "auto", "break", "case", "char", "const", "continue", "default", "do",
    "double", "else", "enum", "extern",	"float", "for",	"goto",	"if",
    "int", "long", "register", "return", "short", "signed",	"sizeof", "static",
    "struct", "switch",	"typedef", "union", "unsigned",	"void",	"volatile",	"while"
]


# 传入源列表，和要保留的字符串
def saveKey(words, keys):
    new_words = []
    for line in words:
        new_line = []
        for word in line:
            for key in keys:
                if key == word:
                    new_line.append(key)
                    break
        if new_line:
            new_words.append(new_line)
    return new_words

# 去掉{}变成嵌套列表
