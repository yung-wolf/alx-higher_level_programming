import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):

    def setUp(self):
        """Set up test cases vars."""
        Base._Base__nb_objects = 0
        self.s1 = Square(5)
        self.s2 = Square(2, 2)
        self.s3 = Square(3, 1, 3)

    def test_id(self):
        """Test ids of square objects."""
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)
        s4 = Square(2, 1, 3, 55)
        self.assertEqual(s4.id, 55)

    def test_attributes(self):
        """Test attributes of square."""
        self.assertEqual(self.s1.width, 5)
        self.assertEqual(self.s1.height, 5)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)

        self.assertEqual(self.s3.width, 3)
        self.assertEqual(self.s3.height, 3)
        self.assertEqual(self.s3.x, 1)
        self.assertEqual(self.s3.y, 3)

    def test_str_print(self):
        """Test magic method __str__ of Square cls."""
        self.assertEqual(str(self.s1), '[Square] (1) 0/0 - 5')
        self.assertEqual(str(self.s2), '[Square] (2) 2/0 - 2')
        self.assertEqual(str(self.s3), '[Square] (3) 1/3 - 3')

    def test_area(self):
        """Test area calc"""
        self.assertEqual(self.s1.area(), 25)
        self.assertEqual(self.s2.area(), 4)
        self.assertEqual(self.s3.area(), 9)

    def test_invlaid_args(self):
        """test invalid args passed to Squre object"""
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s4 = Square('1')
            self.s1.size = [1]
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s4 = Square(-99, 3)
            self.s1.width = 0

    def test_update(self):
        """Test the update() method"""
        self.s1.update(10)
        self.assertEqual(self.s1.id, 10)
        self.s1.update(1, 2)
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s1.size, 2)
        self.s1.update(1, 2, 3, 4)
        self.assertEqual(str(self.s1), '[Square] (1) 3/4 - 2')
        self.s1.update(x=12)
        self.assertEqual(str(self.s1), '[Square] (1) 12/4 - 2')
        self.s1.update(size=7, y=1)
        self.assertEqual(str(self.s1), '[Square] (1) 12/1 - 7')
        self.s1.update(size=7, id=89, y=1)
        self.assertEqual(str(self.s1), '[Square] (89) 12/1 - 7')


