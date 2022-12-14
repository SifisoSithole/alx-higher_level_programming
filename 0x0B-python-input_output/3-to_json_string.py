#!/usr/bin/python3

"""
3-to_json_string module

Returns the JSON represantation of an object
"""


def to_json_string(my_obj):
    """
    Returns the JSON represantation of an object
    parameters:
        my_object (object): Object to convert
    Return:
        String represantation of my_object
    """
    json = __import__('json')
    return json.dumps(my_obj)
