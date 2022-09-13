#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """A square represantation"""

    def __init__(self, size=0):
        """Create a square
        Args:
            size (int): The size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
