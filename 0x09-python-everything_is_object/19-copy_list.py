#!/usr/bin/python3
"""Returns a copy of a list"""


def copy_list(l):
    """
    Returns a copy of a list
    Parameteres:
        l (list): List to copy
    Return:
        new_list (list): Copy of l
    """
    if isinstance(l, list):
        new_list = l[:]
        return new_list
    else:
        return None
