#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''
    Function that prints a sorted dictionary
    :param a_dictionary: dictionary
    :return: nothing
    '''
    for key, value in sorted(a_dictionary.items()):
        print(key + ":", value)
