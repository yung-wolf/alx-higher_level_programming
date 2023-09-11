#!/usr/bin/python3

"""
MODULE: 9-rectangle
Holds one class, Rectangle()
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class meant to model a rectangle."""
    def __init__(self, width, height):
        """Initialize object."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Calculates area of rectangle."""
        return self.__width * self.__height
