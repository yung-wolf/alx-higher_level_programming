#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    '''
    Function to delete key in dictionary
    :param a_dictionary: dictionary
    :param keys: key to delete
    :return: returns new dictionary
    '''
    if key not in a_dictionary:
        return a_dictionary
    del a_dictionary[key]
    return a_dictionary
