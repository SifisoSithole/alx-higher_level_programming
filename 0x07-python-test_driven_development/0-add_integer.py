#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The 0-add_integer module adds two integers
"""


def add_integer(a, b=98):
    """
    Returns the sum of two integers.
    parameters:
        a (int/float): Integer or float
        b (int/float): Integer or float
    Returns:
        The sum of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be a integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be a integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
