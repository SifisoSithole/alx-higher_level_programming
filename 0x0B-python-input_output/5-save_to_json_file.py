#!/usr/bin/python3
"""
5-save_to_json_file module

Writes an object to a text file
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file
    Parameters:
        my_obj (object): Python data structure
        filename (str): File to create
    """
    json = __import__('json')
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
