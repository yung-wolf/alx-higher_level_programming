#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    '''
    Safely print <x> number of elements of a list
    :param my_list: the list to print
    :param x: number of elements to print
    :return: number of elements actually printed
    '''
    count = 0  # count real number actually printed
    try:
        for element in my_list:
            if count < x:
                print(element, end="")
                count += 1
        print()
        return count
    except IndexError:
        return count
