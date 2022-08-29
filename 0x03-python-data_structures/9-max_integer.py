#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxi = -2147483647
    for i in my_list:
        if i > maxi:
            maxi = i
    return maxi
