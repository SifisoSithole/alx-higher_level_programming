#!/usr/bin/python3
"""
1-write_file module.

Writes text to a file
"""


def write_file(filename="", text=""):
    """
    Writes to a text file
    Parameters:
        filename (str): The name of the file
    """
    line = 0
    if text is None or filename is None:
        return line

    with open(filename, 'w', encoding="utf-8") as f:
        line = f.write(str(text))
    return line
