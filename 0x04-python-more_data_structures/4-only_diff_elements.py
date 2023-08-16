#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    '''Function that returns a set of unique elements between two sets.
    set_1: first set
    set_2: second set
    '''

    # return unique elements b/n both sets
    return (set_1 ^ set_2)
