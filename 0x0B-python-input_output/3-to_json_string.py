#!/usr/bin/python3

"""
Module: 3-to_json_string
Has one function, to_json_string()
"""


def to_json_string(obj):
    """A function that returns the JSON representation of an object (string):

    Args:
        obj (object): python object
    """
    if (obj):
        import json
        json_string = json.dumps(obj)
        return json_string
