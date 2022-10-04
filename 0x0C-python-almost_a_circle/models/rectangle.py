#!/usr/bin/python3
"""
Define a Rectangle class

This class will represent a rectangle

This class will contain width, height and coordinates of the rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    A rectangle represantation

    This class will represent a rectangle

    This class will contain width, height and coordinates of the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculates area"""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle"""
        s = " " * self.__x + '#' * self.__width
        [print() for i in range(self.__y)]
        [print(s) for i in range(self.__height)]

    def __str__(self):
        """Overiding the __str__ method"""
        s = f"{self.__x}/{self.__y} - {self.__width}/{self.__height}"
        return f"[{type(self).__name__}] ({self.id}) " + s

    @staticmethod
    def validate(name, value):
        """validates values"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if name == 'x' or name == 'y':
            if value < 0:
                raise ValueError(f"{name} must be >= 0")
        else:
            if value <= 0:
                raise ValueError(f"{name} must be > 0")

    def update(self, *args, **kwargs):
        """Update attributes"""
        if args is None or len(args) == 0:
            if kwargs is not None:
                for key, value in kwargs.items():
                    self.validate(key, value)
                    if key == "id":
                        self.id = value

                    if key == "width":
                        self.__width = value

                    if key == "height":
                        self.__height = value

                    if key == "x":
                        self.__x = value

                    if key == "y":
                        self.__y = value
            return
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]

            if i == 1:
                self.validate("width", args[i])
                self.__width = args[i]

            if i == 2:
                self.validate("height", args[i])
                self.__height = args[i]

            if i == 3:
                self.validate("x", args[i])
                self.__x = args[i]

            if i == 4:
                self.validate("y", args[i])
                self.__y = args[i]

    def to_dictionary(self):
        """Returns a dictionary represantation of Rectangle"""
        my_dict = {}
        my_dict['x'] = self.__x
        my_dict['y'] = self.__y
        my_dict['height'] = self.__height
        my_dict['width'] = self.__width
        my_dict['id'] = self.id

        return my_dict
