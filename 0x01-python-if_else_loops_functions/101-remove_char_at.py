#!/usr/bin/python3
def remove_char_at(str, n):
    cpyStr = ""
    for i in range(len(str)):
        if i != n:
            cpyStr += str[i]
    return cpyStr
