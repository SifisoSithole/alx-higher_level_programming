#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = []
    b = []
    for i in range(2):
        try:
            a.append(tuple_a[i])
        except:
            a.append(0)
    for i in range(2):
        try:
            b.append(tuple_b[i])
        except:
            b.append(0)
    return a[0] + b[0], a[1] + b[1]
