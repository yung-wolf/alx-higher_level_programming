#!/usr/bin/python3

"""
Module: 6-load_from_json_file
Holds one function, load_from_json_file()
"""


def load_from_json_file(filename):
    """Write a function that creates an Object from a “JSON file”:

    Arg:
        filename
    """
    if (filename):
        import json
        with open(filename, "r") as json_file:
            obj = json.load(json_file)
            return obj
