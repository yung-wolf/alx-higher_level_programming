#!/usr/bin/python3

def safe_print_division(a, b):
    '''
    Fuction that divides two numbers and returns the result.
    :param a: first integer
    :param b: second integer
    :return: result of division on success, None on failure
    '''
    ans = 0
    try:
        ans = a / b
    except ZeroDivisionError:
        ans = None
        return None
    finally:
        print("Inside result: {}".format(ans))
        return ans
