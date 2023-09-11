#!/usr/bin/python3

"""
Module: 3-is_same_class
Holds one function, is_kind_of_class()
"""


def is_kind_of_class(obj, a_class):
    """A function that returns True if the object is
    an instance of the specified class or is an insta
    nce of a class that inherited from, the specified
    class; otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
