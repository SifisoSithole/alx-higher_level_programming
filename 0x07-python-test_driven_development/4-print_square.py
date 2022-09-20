#!/usr/bin/python3
"""
This is the 4-print_square module.

The 4-print_square module prints a square of size `size`.
"""


def print_square(size):
    """
    Prints a square of size `size`
    Parameters:
        size (int): Length of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    [print("#" * size) for i in range(size)]
