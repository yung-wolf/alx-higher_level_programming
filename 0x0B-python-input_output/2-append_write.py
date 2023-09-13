#!/usr/bin/python3

"""
Module: 2-append_write
Holds one function, write_file()
"""


def append_write(filename="", text=""):
    """A function that writes a string to a text
    file (UTF8) and returns the num of chars writen
    """
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        num_of_c = len(text)
        return num_of_c
