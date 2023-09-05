#!/usr/bin/python3

"""
Module: 4-print_square
Holds one function, print_square()
"""


def print_square(size):
    """Function that prints a square with the character #.

    Args:
        size (int): length of square.
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    row = size
    shape = ""

    while row != 0:
        shape += '#' * size + '\n'
        row -= 1
    shape = shape[:-1]
    print(shape)
