#!/usr/bin/python3

"""
Module: 1-write_file
Holds one function, write_file()
"""


def write_file(filename="", text=""):
    """A function that writes a string to a text
    file (UTF8) and returns the num of chars writen
    """
    with open(filename, 'w', encoding='utf-8') as f:
        num_bytes_written = f.write(text)
        return num_bytes_written
