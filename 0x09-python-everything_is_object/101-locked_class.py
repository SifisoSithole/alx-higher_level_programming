#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    This class excepts only the first_name instance attribute
    """
    __slots__ = ["first_name"]
