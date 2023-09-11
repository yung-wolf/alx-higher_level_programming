#!/usr/bin/python3
"""
Module: 1-my_list
Holds a class, MyList which inherits from list.
"""


class MyList(list):
    """My custom list."""
    def print_sorted(self):
        """Prints MyList in ascending order."""
        nlist = sorted(self)
        print(nlist)
