#!/usr/bin/python3

def max_integer(my_list=[]):
    '''Function that returns the biggest inte    ger from a list
    '''
    if not my_list:
        return None
    else:
        max_int = -1000
        for num in my_list:
            if num > max_int:
                max_int = num
        return max_int
