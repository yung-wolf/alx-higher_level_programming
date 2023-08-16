#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    '''
    Function that multiplies all elements of list by number
    :param my_list: list arg
    :param number: number arg
    :return: new list of modified values
    '''
    n_list = list(map(lambda x: number * x, my_list))
    return n_list
