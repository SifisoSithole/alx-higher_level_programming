#!/usr/bin/python3
"""
This is the 3-say_my_name module

The `3-say_my_name module prints the first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>
    Parameteters:
        first_name (str): First name
        last_name (str): Last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
