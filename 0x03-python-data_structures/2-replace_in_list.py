#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    '''Function to replace element at index (idx)
    a list (my_list) like in C
    '''
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:  # if index is out of range
        return my_list
    else:
        my_list[idx] = element
        return my_list
