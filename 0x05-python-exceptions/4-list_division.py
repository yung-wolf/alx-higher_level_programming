#!/usr/bin/python3

def list_division(my_list_1, my_list_2, lst_length):
    '''
    A Function that divides element by element of 2 lists.
    :param my_list_1: list 1
    :param my_list_2: list 2
    :param lst_length: length of list
    :return: new list with all divisions
    '''
    nlist = []
    count = 0

    while count < lst_length:
        try:
            ans = my_list_1[count] / my_list_2[count]
        except ZeroDivisionError:
            print("division by 0")
            ans = 0
        except TypeError:
            print("wrong type")
            ans = 0
        except IndexError:
            print("out of range")
            ans = 0
        finally:
            nlist.append(ans)
        count += 1
    return nlist
