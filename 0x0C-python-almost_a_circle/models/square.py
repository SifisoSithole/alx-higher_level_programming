#!/usr/bin/python3
from models.rectangle import Rectangle
"""Defines a square and coordinates"""


class Square(Rectangle):
    """Represantation of a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        self.validate("width", size)
        self.width = size
        self.height = size

    def __str__(self):
        """Sting represantation of an instance"""
        s = super().__str__()
        s = s.split("-")
        return s[0] + "- " + str(self.width)

    def update(self, *args, **kwargs):
        """Update attributes"""
        if args is None or len(args) == 0:
            if kwargs is not None:
                for key, value in kwargs.items():
                    self.validate(key, value)
                    if key == "id":
                        self.id = value

                    if key == "size":
                        self.width = value
                        self.height = value

                    if key == "x":
                        self.x = value

                    if key == "y":
                        self.y = value
            return
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]

            if i == 1:
                self.validate("width", args[i])
                self.width = args[i]
                self.height = args[i]

            if i == 2:
                self.validate("x", args[i])
                self.x = args[i]

            if i == 3:
                self.validate("y", args[i])
                self.y = args[i]

    def to_dictionary(self):
        """Returns dictionary representation of a Square"""
        my_dict = {}
        my_dict['id'] = self.id
        my_dict['x'] = self.x
        my_dict['size'] = self.width
        my_dict['y'] = self.y

        return my_dict
