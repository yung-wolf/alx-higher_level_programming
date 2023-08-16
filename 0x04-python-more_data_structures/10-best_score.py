#!/usr/bin/python3

def best_score(a_dictionary):
    '''
    A function that returns the key with the biggest integer value
    :param a_dictionary: dictionary
    :return: key (possibly be a string)
    '''

    # handle case of No dictionary being entered
    if not a_dictionary:
        return None

    max_int = 0

    for key, value in a_dictionary.items():
        if value > max_int:  # check if value is bigger than max_int
            max_int = value  # for True, assign value to max_int
            d_key = key  # and the key of value to d_key

    return d_key
