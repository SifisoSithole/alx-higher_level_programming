#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """A square represantation"""

    def __init__(self, size=0):
        """Create a square
        Args:
            size (int): The size of the square
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, num):
        """Set the size of the square"""
        if type(num) is not int:
            raise TypeError("size must be an integer")
        if num < 0:
            raise ValueError("size must be >= 0")
        self.__size = num

    def area(self):
        """Return area of Square"""
        return (self.__size ** 2)
