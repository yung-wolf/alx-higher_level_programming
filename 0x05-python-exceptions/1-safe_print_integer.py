#!/usr/bin/python3

def safe_print_integer(value):
    '''
    Only prints an integer.
    :param value: value to print
    :return: true if integer, False if not integer
    '''
    try:
        if value // 10:
            print("{:d}".format(value), end="\n")
            return True
    except TypeError:
        return False
