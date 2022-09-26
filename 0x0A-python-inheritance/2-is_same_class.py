#!/usr/bin/pythone3
"""
This is the 2-is_same_class module

It tests if an object belongs in a class or not
"""


def is_same_class(obj, a_class):
    """
    Tests if an object belongs to a class or not
    Parameter:
        obj (object): Object
        a_class (class): Class
    Return:
        True if instance otherwise False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
