#!/usr/bin/python3
""" Define a subclass of list """


class MyList(list):
    """Subclass of the list class"""
    def print_sorted(self):
        print(sorted(self))
