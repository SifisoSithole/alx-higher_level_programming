#!/usr/bin/python3
"""
0-read_file module.

Reads from a file and prints to stdout
"""


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout
    Parameters:
        filename (str): The name of the file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        line = f.readline()
        while line != '':
            print(line, end='')
            line = f.readline()
