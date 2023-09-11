#!/usr/bin/python3

"""
Module: 4-inherits_from
Holds one function, inherits_from()
"""


def inherits_from(obj, a_class):
    """Function returns True if the object is an
    instance of a class that inherited (directly or
    indirectly) from the specified class ; otherwise False

    Args:
        obj (any): object of any type
        a_class (class): class
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return (True)
    else:
        return (False)
