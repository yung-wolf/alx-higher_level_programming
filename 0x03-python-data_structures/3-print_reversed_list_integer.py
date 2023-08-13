#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    '''Function to print a list of ints in reverse
    '''
    while my_list: #print last num in list untill list is empty
        num = my_list.pop()
        print("{:d}".format(num))
