#!/usr/bin/python3

"""
Module: 0-read_file
Holds one function, read_file()
"""


def read_file(filename=""):
    """Function that reads text file. Prints text
    to stdout.

    Args:
        filename (str): name of file
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
