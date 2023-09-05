#!/usr/bin/python3

"""
Module: 5-text_indentation.py
Holds one function, text_indentation(text)
"""


def text_indentation(text):
    """Function that prints a text with 2 new lines after each of these
    characters: `.`, `?` and `:`
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    i = 0
    _str = ""
    x = list(text)
    prev_len_text = len(text)
    new_len_text = len(text)

    while i < new_len_text:
        if x[i] == '.' or x[i] == ':' or x[i] == '?':
            if i == (len(x) - 1):
                x.append('\n\n')
            elif x[i + 1] == " ":
                x[i + 1] = '\n\n'
            else:
                x.append('E')  # shift the list to the right to make space for
                new_len_text = len(x)  # new line char
                loop_counter = new_len_text - i - 2
                last_ele = -1  # last index in list
                before_last_ele = -2  # before last index in list / text
                z = 0  # counter
                while z < loop_counter:
                    x[last_ele] = x[before_last_ele]
                    last_ele -= 1
                    before_last_ele -= 1
                    z += 1
                x[i + 1] = '\n\n'
        i += 1

    for c in x:
        _str += c

    # print formatted text
    print(_str, end="")
