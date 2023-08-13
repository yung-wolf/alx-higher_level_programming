#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    '''Function to replace element at index (idx)
    of list (my_list) without modifying the original copy
    '''
    if idx < 0:
        return my_list[:]
    elif idx > len(my_list) - 1: #if index is out of range
        return my_list[:]
    else: # makes a copy of list
        cpy_my_list = my_list[:]
        cpy_my_list[idx] = element #changes element in copy without modifying the original
        return cpy_my_list  
