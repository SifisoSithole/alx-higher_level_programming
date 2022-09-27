#!/usr/bin/python3
"""
2-append_write module.

Appends text to a file
"""


def append_write(filename="", text=""):
    """
    Appends to a text file
    Parameters:
        filename (str): The name of the file
        text (str): Text to append to a file
    """
    line = 0
    if text is None or filename is None:
        return line

    with open(filename, 'a', encoding="utf-8") as f:
        line = f.write(str(text))
    return line
