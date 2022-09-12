#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    if my_list is None or x is None:
        return num
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except ValueError:
            continue
        except TypeError:
            continue
        else:
            num += 1
    print()
    return num
