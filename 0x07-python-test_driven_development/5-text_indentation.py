#!/usr/bin/python3
"""
This is the 5-text_indentation module.

Prints text with 2 new lines after each of these characters: ".", "?" and ":"
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each of
    these characters: ".", "?" and ":"
    Parameters:
        text (str): String to print
    """
    print_c = True
    if isinstance(text, str):
        for c in text:
            if c == "." or c == "?" or c == ":":
                print(c + "\n")
                print_c = False
            else:
                if print_c:
                    print(c, end="")
                else:
                    print_c = True
    else:
        raise TypeError("text must be a string")
