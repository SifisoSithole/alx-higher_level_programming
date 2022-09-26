#!/usr/bin/python3
"""
This is the 0-lookup module.

The 0-lookup module returns a list of available attributes and
methods of an object
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object
    Parameter:
        obj (object): Object
    Return:
        list of available attributes and methods of an object
    """

    return dir(obj)

