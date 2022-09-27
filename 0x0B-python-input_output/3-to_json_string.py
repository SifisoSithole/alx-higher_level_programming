#!/usr/bin/python3
import json
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
    return json.dumps(my_obj)
