#!/usr/bin/python3

"""
4-from_json_string module

Returns the JSON represantation of an object
"""


def from_json_string(my_str):
    """
    Returns the python data structure represanted by a JSON string
    parameters:
        my_str (str): String
    Return:
        Python data structure
    """
    json = __import__('json')
    return json.loads(my_str)
