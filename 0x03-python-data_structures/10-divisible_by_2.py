#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    '''Function that finds all the multiples     of 2 in a list
    '''
    
    # make copy of list
    new_list = my_list[:]
    index = 0

    for num in new_list:
        if num % 2 == 0:
            new_list[index] = True
        else:
            new_list[index] = False
        index += 1
     
    return new_list
