#!/usr/bin/python3

"""
Module: 5-save_to_json_file
Holds one function, save_to_json_file()
"""


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file
    , using a JSON representation:

    Args:
        my_obj (obj): python object
        filename (file): json file
    """
    import json
    with open(filename, 'w') as json_file:
        json.dump(my_obj, json_file)
