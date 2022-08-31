#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    item = a_dictionary.copy()
    item = item.items()
    for tup in item:
        if tup[1] == value:
            a_dictionary.pop(tup[0])
    return a_dictionary
