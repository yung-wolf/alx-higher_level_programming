#!/usr/bin/python3
'''
Module 5-square
class that defines a square by: (based on 4-square.py)
Public instance method: def my_print(self):
that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
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

    @property
    def size(self):
        '''
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'

        @size.setter:
            check if value is an integer before assigning it to size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        '''
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'

        Gets the current area of a square

        Returns:
            current square area if successful
        '''
        return self.__size * self.__size

    def my_print(self):
        '''
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'

        Public instance method: def my_print(self):
        that prints in stdout the square with the
        character #:
        if size is equal to 0, print an empty line
        '''

        #: int: holds size of square in var self.row & self.column
        self.row = self.__size
        self.column = self.__size

        if self.__size == 0:
            print()
        else:
            while self.column > 0:
                while self.row > 0:
                    if self.row != 1:
                        print('#', end="")
                    else:
                        print('#')
                    self.row -= 1
                self.column -= 1
                self.row = self.__size
