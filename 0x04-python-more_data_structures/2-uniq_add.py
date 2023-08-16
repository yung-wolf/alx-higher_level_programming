#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''
    Funtion that adds unique elements of my_list. Elements are added only once.
    :param my_list: list
    :return: sum of elements on success
    '''
    new_list = set(my_list)
    ans = 0
    for num in new_list:
        ans += num

    return ans
