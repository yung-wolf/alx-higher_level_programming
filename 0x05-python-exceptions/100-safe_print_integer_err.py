#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    '''
    Only prints an integer.
    :param value: value to print
    :return: true if integer, False if not integer
    '''
    try:
        print("{:d}".format(value), end="\n")
        return True
    except ValueError as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
