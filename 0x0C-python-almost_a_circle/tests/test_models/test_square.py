#!/usr/bin/pythone3

from models.square import Square
import unittest

"""unittests for Square class"""


class TestSquare(unittest.TestCase):

    def test_inheritance(self):
        """Test inheritance and the __init__ method"""
        s1 = Square(5)

        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 13)
        self.assertEqual(s1.area(), 25)
        self.assertEqual(str(s1), "[Square] (13) 0/0 - 5")

    def test_data_validation(self):
        """Test data validation"""

        with self.assertRaises(ValueError):
            Square(-5, 0, 0, 2)

        with self.assertRaises(TypeError):
            Square({}, 0, 0, 3)

        with self.assertRaises(ValueError):
            Square(4, -1, 3, 4)

        with self.assertRaises(TypeError):
            Square(5, 4, "10", 5)

    def test_size(self):
        """Test the getter and setter for size"""
        s1 = Square(6, 0, 0, 6)
        self.assertEqual(s1.size, 6)
        self.assertEqual(str(s1), "[Square] (6) 0/0 - 6")

        s1.size = 8
        self.assertEqual(s1.size, 8)

        with self.assertRaises(TypeError):
            s1.size = {}

        with self.assertRaises(ValueError):
            s1.size = -5

    def test_update_args_1(self):
        """Test the update method"""

        s1 = Square(4, 9, 7, 26)
        s1.update(10, 10, 10, 10)
        s2 = Square(4, 3, 10, 27)
        s2.update(10, 10, 10, 10)
        s3 = Square(12, 8, 6, 28)
        s3.update(10, 10, 10, 10)

        self.assertEqual(str(s1), "[Square] (10) 10/10 - 10")
        self.assertEqual(str(s2), "[Square] (10) 10/10 - 10")
        self.assertEqual(str(s3), "[Square] (10) 10/10 - 10")

    def test_update_args_2(self):
        """Test the validation of update"""
        s1 = Square(4, 5, 3, 29)

        with self.assertRaises(ValueError):
            s1.update(29, -10, 10, 10)

        with self.assertRaises(TypeError):
            s1.update(29, 10, "10", 10)

        with self.assertRaises(ValueError):
            s1.update(29, -10, 0, 10)

        with self.assertRaises(TypeError):
            s1.update(29, 10, 10, {})

    def test_update_kwargs(self):
        """Test kwargs in update"""
        s1 = Square(4, 5, 7, 26)
        s1.update(id=10)
        s1.update(size=10)
        s1.update(x=30)
        s1.update(y=40)
        s2 = Square(4, 5, 7, 26)
        s2.update(9, 9, 9, id=40, size=20)

        self.assertEqual(s1.id, 10)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 30)
        self.assertEqual(s1.y, 40)
        self.assertEqual(str(s2), "[Square] (9) 9/7 - 9")

    def test_dictionary(self):
        """Test to_dictionary method"""
        r1 = Square(10, 1, 9, 27)
        my_dict = {'id': 27, 'x': 1, 'size': 10, 'y': 9}
        self.assertEqual(r1.to_dictionary(), my_dict)
        self.assertEqual(type(r1.to_dictionary()), dict)
