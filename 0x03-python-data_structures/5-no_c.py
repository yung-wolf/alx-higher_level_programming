#!/usr/bin/python3

def no_c(my_string):
    '''A function to remove all chars <c> and    <C> from string
    '''
    new_string = ""

    # loop thru string to remove c & C
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
