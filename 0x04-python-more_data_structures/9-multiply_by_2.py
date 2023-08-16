#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    '''
    A funtion that multiplies all values of dictionary by 2
    :param a_dictionary: deictionary
    :return: new modified dictionary
    '''
    n_dict = {}

    for k, v in a_dictionary.items():
        n_dict[k] = v * 2

    return n_dict
