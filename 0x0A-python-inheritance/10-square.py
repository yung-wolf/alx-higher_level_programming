#!/usr/bin/python3

"""
Module: 10-square
Holds a class, Square()
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Models a square. Inherits from Rectangle."""
    def __init__(self, size):
        """Initializes object."""
        self.integer_validator("size", size)
        self.__size = size
        self._Rectangle__width = self._Rectangle__height = self.__size = size
