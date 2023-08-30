#!/usr/bin/python3
'''
Module 2-square
Class that defines a square by: (based on 1-square.py)

Private instance attribute: size
'''


class Square:
    '''
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'

    Models a square

    Attributes:
        size (int): size of square
    '''
    def __init__(self, size=0):
        '''Initializes the class

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'

        Args:
            size (int): size of square of type int, default size=0

        '''
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
