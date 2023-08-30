#!/usr/bin/python3
'''
Module 6-square
Private instance attribute: position:
property def position(self): to retrieve it
property setter def position(self, value): to set it:

Instantiation with optional size and optional
position: def __init__(self, size=0, position=(0, 0)):
'''


class Square:
    '''
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'

    Models a square

    Attributes:
        __size (int): size of square
        __position (tuple): co-ordinates of square
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''Initializes the class

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'

        Args:
            __size (int): size of square of type int, default size=0
            __position(tuple): of type int, co-ordinates of square
        '''
        self.__size = size
        self.__position = position

        try:
            isinstance(self.__size, int)
            if self.__size < 0:
                raise ValueError
        except TypeError as err:
            print("size must be an integer")
        except ValueError as err:
            print("size must be >= 0")

    @property
    def position(self):
        '''
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'

        @position.setter:
            set position if value has 2 positive integer
            else raise TypeError
        '''
        return self.__position

    @position.setter
    def position(self, value):
        self.check = 0  # check for negative num in value
        for num in value:
            if num >= 0:
                check = 0
            else:
                check = 1
                break

        if check == 1:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            size.__position = value

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

        position should be use by using space-
        Don’t fill lines by spaces when position[1] > 0
        '''

        #: int: holds size of square in var self.row & self.column
        self.row = self.__size
        self.column = self.__size

        if self.__size == 0:
            print()
        else:
            while self.column > 0:
                for num in range(self.__position[0]):
                    print(" ", end="")
                while self.row > 0:
                    if self.row != 1:
                        print('#', end="")
                    else:
                        print('#')
                    self.row -= 1
                self.column -= 1
                self.row = self.__size
