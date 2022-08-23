#!/usr/bin/python3
for first in range(0, 9):
    for second in range(first + 1, 10):
        if first != 8:
            print("{0}{1}".format(first, second), end=", ")
        else:
            print("{0}{1}".format(first, second))
