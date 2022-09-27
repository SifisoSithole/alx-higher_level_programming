#!/usr/bin/python3
""" Define student class """


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Initialize"""
        if not isinstance(first_name, str):
            raise TypeError("first_name must be string")
        self.first_name = first_name
        if not isinstance(last_name, str):
            raise TypeError("last_name must be string")
        self.last_name = last_name
        if not isinstance(age, int):
            raise TypeError("age must be an integer")
        self.age = age

    def to_json(self):
        """String represantation"""
        return vars(self)
