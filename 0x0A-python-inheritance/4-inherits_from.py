#!/usr/bin/python3
"""
This is the 4-inherits module

It tests if an obj inherits from class
"""


def inherits_from(obj, a_class):
    """
    Tests if an obj inherits from a_class
    Parameters:
        obj (object): Object
        a_class (class): Class
    Return:
        True if obj is an instance of a_class, otherwise false
    """
    
    return isinstance(obj, a_class) and type(obj) != a_class
