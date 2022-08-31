#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total = 0
    divisor = 0
    for tup in my_list:
        total += tup[0] * tup[1]
        divisor += tup[1]
    return total / divisor
