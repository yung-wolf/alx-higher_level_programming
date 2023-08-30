#!/usr/bin/python3
'''
Module 3-square
class that defines a square by: (based on 2-square.py
Private instance attribute: size
Public instance method: def area(self)
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

    def area(self):
        '''
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'

        Gets the current area of a square

        Returns:
            current square area if successful
        '''
        return self.__size * self.__size
