#!/usr/bin/python3
"""Define a BaseGeometry class"""


class BaseGeometry:
    """Super class"""
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")
