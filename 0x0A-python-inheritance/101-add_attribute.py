#!/usr/bin/python3

"""
Module: 101-add_attribute
Holds one function, add_attribute()
"""


def add_attribute(mc, name="", value=""):
    """Adds an attribute to a class if possible."""
    if isinstance(mc, (str, int, bool, list, dict, float, tuple, set)):
        raise TypeError("can't add new attribute")
    else:
        mc.name = value
