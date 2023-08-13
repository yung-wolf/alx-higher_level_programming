#!/usr/bin/python3

def element_at(my_list, idx):
    '''Function to retrieves an element from
    a list like in C
    '''
    if idx < 0:
        return None
    elif idx > len(my_list) - 1:  # if index is out of range
        return None
    else:
        return my_list[idx]
