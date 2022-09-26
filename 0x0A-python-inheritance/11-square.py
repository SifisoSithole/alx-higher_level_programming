#!/usr/bin/python3
"""Define a BaseGeometry class"""


class BaseGeometry:
    """Super class"""
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integers"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle represantation"""
    def __init__(self, width, height):
        """Intialize rectangle"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area"""
        return self.__width * self.__height

    def __str__(self):
        """return rectangle"""
        return "[{}] {}/{}".format(type(self).__name__, self.__width, self.__height)


class Square(Rectangle):
    """Square represantation"""
    def __init__(self, size):
        super().integer_validator(size, size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return super().area()
