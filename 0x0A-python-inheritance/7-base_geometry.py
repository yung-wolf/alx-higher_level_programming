#!/usr/bin/python3

"""
MODULE: 7-base_geometry
Holds one class, BaseGeometry()
"""


class BaseGeometry:
    """A class meant to model a geometry shape."""

    def area(self):
        """Gets area of geometry."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value == int."""
        if not type(value) is int:
            raise TypeError(f'{name} must be an integer')
        elif value <= 0:
            raise ValueError(f'{name} must be greater than 0')
