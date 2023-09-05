#!/usr/bin/python3
"""
Module: 6-max_integer_test
Holds unittests for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.3, 3.6, 4.8]), 4.8)
        self.assertEqual(max_integer([-1.5, -2.3, -3.1, -4.9]), -1.5)
        self.assertEqual(max_integer([1.3, 2.0, -3.2, -4.8]), 2.0)

    def test_largeList(self):
        self.assertEqual(max_integer(list(range(1, 20001))), 20000)
        self.assertEqual(max_integer(list(range(-10001, 2))), 1)


    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
