#!/usr/bin/python3

"""
Module: 4-from_json_string
Holds one function, from_json_string()
"""


def from_json_string(my_str):
    """Function that returns an object (Python data
    structure) represented by a JSON string:

    Args:
        my_str (str): string json object
    """
    if (str):
        import json
        obj = json.loads(my_str)
        return obj
