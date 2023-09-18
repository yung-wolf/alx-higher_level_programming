import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_no_id_passed(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_arg_passed(self):
        b99 = Base(12)
        self.assertEqual(b99.id, 12)

    def test_multiple_instances(self):
        b1 = Base(14)
        b2 = Base()
        b3 = Base()
        b4 = Base(99)
        b5 = Base()
        b6 = Base(0)
        self.assertEqual(b1.id, 14)
        self.assertEqual(b2.id, 1)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 99)
        self.assertEqual(b5.id, 3)
        self.assertEqual(b6.id, 0)

    def test_neg_id(self):
        b1 = Base(-1)
        self.assertEqual(b1.id, -1)

