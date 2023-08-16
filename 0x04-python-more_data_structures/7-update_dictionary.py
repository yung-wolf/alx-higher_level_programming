#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    '''
    Function that replaces or adds key/value to dictionary
    :param a_dictionary: dictionary
    :param key: key
    :param value: value
    :return:
    '''
    a_dictionary[key] = value
    return a_dictionary
