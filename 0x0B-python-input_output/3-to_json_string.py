#!/usr/bin/python3

"""
Module: 3-to_json_string
Has one function, to_json_string()
"""


def to_json_string(my_obj):
    """A function that returns the JSON representation of an object (string):

    Args:
        obj (object): python object
    """
    import json
    json_string = json.dumps(my_obj)
    return json_string
