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
        self.__size = size

        try:
            isinstance(self.__size, int)
            if self.__size < 0:
                raise ValueError
        except TypeError as err:
            print("size must be an integer")
        except ValueError as err:
            print("size must be >= 0")
