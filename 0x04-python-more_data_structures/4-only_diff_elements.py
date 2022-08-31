#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set_1.copy()
    new_set.update(set_2)
    for ele in set_1:
        if ele in set_2:
            new_set.remove(ele)
    set_1.update(set_2)
    return new_set
