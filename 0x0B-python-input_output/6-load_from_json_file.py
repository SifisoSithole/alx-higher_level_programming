#!/usr/bin/python3
"""
6-load_from_json_file module

Creates an Object from a “JSON file”
"""


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”
    """
    json = __import__('json')
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
