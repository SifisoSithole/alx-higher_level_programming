#!/usr/bin/python3
"""
This is the 3-is_kind_of_class module

It tests if an object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    Tests if an object is an instance of a class
    Parameters:
        obj (object): Object
        a_class (class): Class
    Return:
        True if obj is an instance of a_class, otherwise false
    """
    return isinstance(obj, a_class)
