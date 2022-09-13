#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """A square represantation"""

    def __init__(self, size=0, position=(0, 0)):
        """Create a square
        Args:
            size (int): The size of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square"""
        return (self.__position)

    @position.setter
    def position(self, v):
        """Set the position of the square"""
        if type(v) is not tuple or len(v) != 2 or v[0] < 0 or v[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = v

    def area(self):
        """Return area of Square"""
        return (self.__size ** 2)

    def my_print(self):
        """Print the square"""
        for i in range(self.__size):
            for i in range(self.size):
                print("#", end="")
            print()
        if not self.__size:
            print()

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
