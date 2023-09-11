#!/usr/bin/python3

"""
MODULE: 6-base_geometry
Holds one class, BaseGeometry()
"""


class BaseGeometry:
    """A class meant to model a geometry shape."""

    def area(self):
        """Gets area of geometry."""
        raise Exception("area() is not implemented")
