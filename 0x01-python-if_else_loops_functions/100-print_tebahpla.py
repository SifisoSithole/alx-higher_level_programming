#!/usr/bin/python3
uppercase = False
for i in range(122, 96, -1):
    c = i
    if uppercase:
        c -= 32
        uppercase = False
    else:
        uppercase = True
    print("{:c}".format(c), end='')
