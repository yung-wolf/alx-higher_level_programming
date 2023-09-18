import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        """Set up test class."""
        Base._Base__nb_objects = 0
        self.r1 = Rectangle(3, 2)
        self.r2 = Rectangle(4, 1)
        self.r3 = Rectangle(5, 3, 0, 0, 12)

    def test_rect_id(self):
        """Test rect ids."""
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 12)


    def test_attribute(self):
        """Test rect attributes."""
        self.assertEqual(self.r1.width, 3)
        self.assertEqual(self.r2.height, 1)
        self.assertEqual(self.r3.width, 5)
        self.assertEqual(self.r3.height, 3)
        self.assertEqual(self.r3.x, 0)
        self.assertEqual(self.r3.y, 0)

    def test_validate_attributes(self):
        """Test attribute validation of rect."""
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle('10', 2)
            self.width = [1]
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(2, [2])
            self.height = 'e'
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(10, 2, {'e':3}, 5)
            self.x = [1]
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(10, 2, 5, 't')
            self.y = [1]

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            self.r1.width = -10
            Rectangle(-1, 2, 4, 4, 9)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            self.r1.height = -1
            Rectangle(3, -2, 7, 7)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            self.r1.x = -1
            Rectangle(1, 2, -1, 3, 55)
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            self.r1.y = -1
            Rectangle(1, 2, 1, -3)

    def test_area(self):
        """Test area."""
        self.assertEqual(self.r1.area(), 6)
        self.assertEqual(self.r2.area(), 4)
        self.assertEqual(self.r3.area(), 15)

    def test_invalid_args(self):
        """Test invalid args passed to class."""
        self.assertRaises(TypeError, Rectangle, 1)
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 4, 5, 6, 7, 8, 9)

    def test_str_print(self):
        """Test magic str print method."""
        self.assertEqual(str(self.r1), '[Rectangle] (1) 0/0 - 3/2')
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 99)), '[Rectangle] (99) 2/1 - 4/6')

    def test_update(self):
        """Test the update method of REct.

        Test *args positional arg & Test **kwargs - keyword args
        """
        self.r1.update(89)
        self.assertEqual(str(self.r1), '[Rectangle] (89) 0/0 - 3/2')
        self.r1.update(89, 2, 3)
        self.assertEqual(str(self.r1), '[Rectangle] (89) 0/0 - 2/3')
        self.r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(self.r1), '[Rectangle] (89) 4/5 - 2/3')

        self.r3.update(height=1)
        self.assertEqual(str(self.r3), '[Rectangle] (12) 0/0 - 5/1')
        self.r3.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(self.r3), '[Rectangle] (89) 3/1 - 2/1')

