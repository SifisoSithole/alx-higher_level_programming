#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return []
    new_list = my_list.copy()
    if search in my_list:
        i = my_list.index(search)
        new_list[i] = replace
    return new_list
