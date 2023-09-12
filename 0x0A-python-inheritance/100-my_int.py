#!/usr/bin/python3

"""
Module: 100-my_int
Holds one class, MtInt()
"""


class MyInt(int):
    """Custom class of int. Inherits from int."""
    def __init__(self, value):
        """Initialze object."""
        self.value = value

    def __eq__(self, other):
        if isinstance(other, MyInt):
            return self.value != other.value
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
