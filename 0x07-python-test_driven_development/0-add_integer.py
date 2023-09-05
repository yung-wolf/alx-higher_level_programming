#!/usr/bin/python3

"""
Module: 0-add_integer

Holds one function, add_integer()
"""


def add_integer(a, b=98):
    """A function that adds two integers.

    Args:
        a (int/ float): first num
        b (int/ float): second num (default=89)
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    elif type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)
