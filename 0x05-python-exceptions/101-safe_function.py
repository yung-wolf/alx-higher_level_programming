#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    '''
    A Function that safely executes another function.
    :param fct: pointer to function to execute
    :param args: argument(s)
    :return: result of function on success, None on failure
    '''
    result = 0

    try:
        result = fct(*args)
    except Exception as zer:
        print("Exception: {}".format(zer), file=sys.stderr)
        result = None
    return result
