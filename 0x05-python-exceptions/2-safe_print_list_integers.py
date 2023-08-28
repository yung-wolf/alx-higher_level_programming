#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    '''
    Only prints an integer.
    :param value: value to print
    :return: true if integer, False if not integer
    '''
    count = 0
    num = 0
    while count < x:
        y = my_list[count]
        try:
            if y / 1:
                print("{:d}".format(y), end="")
                num += 1
        except TypeError:
            print(end="")
        count += 1

    print()
    return num
