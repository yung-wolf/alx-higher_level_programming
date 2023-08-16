#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''
    :param my_list: list
    :param search: value in list to replace
    :param replace: value to replace <search> with
    :return: new list of modified values
    '''

    new_list = [replace if item == search else item for item in my_list]

    return new_list
