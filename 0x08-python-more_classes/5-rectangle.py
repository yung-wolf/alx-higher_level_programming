#!/usr/bin/python3
'''
Module: 5-rectangle
Has one class, Rectangle()

rectangle == rect
'''


class Rectangle:
    '''Models a Rectangle.

    Instance Attributes:
        width (int): width of rect
        height (int): height of rect
    '''

    def __init__(self, width=0, height=0):
        '''Initialze class with optional attributes'''
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

    def __str__(self):
        '''Prints the area of rect with the char `#`'''
        self.column = self.__width
        self.row = self.__height
        shape = ""

        while self.row != 0:
            shape += '#' * self.__width + '\n'
            self.row -= 1
        return shape[:-1]

        if self.__width == 0 or self.__height == 0:
            return ""

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")

    @property
    def width(self):
        '''Retrieve width value of rect'''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        '''Retrieve the height value of rect'''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        '''Returns the area of rect.'''
        return self.__width * self.__height

    def perimeter(self):
        '''Returns the perimeter of rect.'''
        self.result = (2 * self.__width) + (2 * self.__height)
        if self.__width == 0 or self.__height == 0:
            self.result = 0
        return self.result
