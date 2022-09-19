#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """A Rectangle represantation"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Creates a rectangle
        Parameters:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    def __del__(self):
        """Prints message when instance deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Define the print represantation of a rectangle"""
        str_rep = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for height in range(self.__height):
            for width in range(self.__width):
                str_rep += str(self.print_symbol)
            if height < self.__height - 1:
                str_rep += "\n"
        return str_rep

    def __repr__(self):
        """Returns a string represantation of a rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
