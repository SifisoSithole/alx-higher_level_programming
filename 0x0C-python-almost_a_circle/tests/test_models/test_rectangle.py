#!/usr/bin/pythone3

from models.rectangle import Rectangle
import unittest

"""unittests for Rectangle class"""


class TestRectangle(unittest.TestCase):

    def test_id(self):
        """Testing id functionality"""
        rectangle_1 = Rectangle(4, 5, 0, 0)
        rectangle_2 = Rectangle(4, 5, 0, 0, 23)
        rectangle_3 = Rectangle(4, 5, 0, 0)

        self.assertEqual(rectangle_1.id, 1)
        self.assertEqual(rectangle_2.id, 23)
        self.assertEqual(rectangle_3.id, 2)

    def test_data_types(self):
        """Testing data types"""
        rectangle_4 = Rectangle(4, 5, 4, 3, 7)

        self.assertEqual(rectangle_4.width, 4)
        self.assertEqual(rectangle_4.height, 5)
        self.assertEqual(rectangle_4.x, 4)
        self.assertEqual(rectangle_4.y, 3)

        with self.assertRaises(TypeError):
            Rectangle("a", 5, 4, 3, 8)

        with self.assertRaises(TypeError):
            Rectangle(4, {}, 4, 3, 8)

        with self.assertRaises(TypeError):
            Rectangle(4, 6, [], 3, 9)

        with self.assertRaises(TypeError):
            Rectangle(4, 5, 4, (1, ), 8)

    def test_values(self):
        """Test values"""

        rectangle_4 = Rectangle(4, 5, 4, 3, 7)

        self.assertEqual(rectangle_4.width, 4)
        self.assertEqual(rectangle_4.height, 5)
        self.assertEqual(rectangle_4.x, 4)
        self.assertEqual(rectangle_4.y, 3)

        with self.assertRaises(ValueError):
            Rectangle(-3, 5, 4, 3, 8)

        with self.assertRaises(ValueError):
            Rectangle(4, 0, 4, 3, 8)

        with self.assertRaises(ValueError):
            Rectangle(4, 6, -1, 3, 9)

        with self.assertRaises(ValueError):
            Rectangle(4, 5, 4, -10, 8)

    def test_area(self):
        """Test the area method"""

        rectangle_5 = Rectangle(4, 5, 0, 0, 20)
        rectangle_6 = Rectangle(4, 10, 0, 0, 21)
        rectangle_7 = Rectangle(12, 13, 0, 0, 22)

        self.assertEqual(rectangle_5.area(), 20)
        self.assertEqual(rectangle_6.area(), 40)
        self.assertEqual(rectangle_7.area(), 156)

    def test__str__(self):
        """Test the __str__ method"""
        rectangle_8 = Rectangle(4, 5, 9, 7, 23)
        rectangle_9 = Rectangle(4, 10, 3, 10, 24)
        rectangle_10 = Rectangle(12, 13, 8, 6, 25)

        self.assertEqual(str(rectangle_8), "[Rectangle] (23) 9/7 - 4/5")
        self.assertEqual(str(rectangle_9), "[Rectangle] (24) 3/10 - 4/10")
        self.assertEqual(str(rectangle_10), "[Rectangle] (25) 8/6 - 12/13")

    def test_update_args_1(self):
        """Test the update method"""

        rectangle_11 = Rectangle(4, 5, 9, 7, 26)
        rectangle_11.update(10, 10, 10, 10, 10)
        rectangle_12 = Rectangle(4, 10, 3, 10, 27)
        rectangle_12.update(10, 10, 10, 10, 10)
        rectangle_13 = Rectangle(12, 13, 8, 6, 28)
        rectangle_13.update(10, 10, 10, 10, 10)

        self.assertEqual(str(rectangle_11), "[Rectangle] (10) 10/10 - 10/10")
        self.assertEqual(str(rectangle_12), "[Rectangle] (10) 10/10 - 10/10")
        self.assertEqual(str(rectangle_13), "[Rectangle] (10) 10/10 - 10/10")

    def test_update_args_2(self):
        """Test the validation of update"""

        rectangle_14 = Rectangle(4, 5, 4, 3, 29)

        with self.assertRaises(ValueError):
            rectangle_14.update(29, -10, 10, 10, 10)

        with self.assertRaises(TypeError):
            rectangle_14.update(29, 10, "10", 10, 10)

        with self.assertRaises(ValueError):
            rectangle_14.update(29, -10, 10, 0, 10)

        with self.assertRaises(TypeError):
            rectangle_14.update(29, 10, 10, 10, {})

    def test_update_kwargs(self):
        """Test kwargs in update"""
        rectangle_15 = Rectangle(4, 5, 9, 7, 26)
        rectangle_15.update(id=10)
        rectangle_15.update(width=10)
        rectangle_15.update(height=20)
        rectangle_15.update(x=30)
        rectangle_15.update(y=40)
        rectangle_16 = Rectangle(4, 5, 9, 7, 26)
        rectangle_16.update(9, 9, 9, id=40, height=20)

        self.assertEqual(rectangle_15.id, 10)
        self.assertEqual(rectangle_15.width, 10)
        self.assertEqual(rectangle_15.height, 20)
        self.assertEqual(rectangle_15.x, 30)
        self.assertEqual(rectangle_15.y, 40)
        self.assertEqual(str(rectangle_16), "[Rectangle] (9) 9/7 - 9/9")

    def test_dictionary(self):
        """Test to_dictionary method"""
        r1 = Rectangle(10, 2, 1, 9, 27)
        my_dict = {'x': 1, 'y': 9, 'id': 27, 'height': 2, 'width': 10}
        self.assertEqual(r1.to_dictionary(), my_dict)
        self.assertEqual(type(r1.to_dictionary()), dict)
