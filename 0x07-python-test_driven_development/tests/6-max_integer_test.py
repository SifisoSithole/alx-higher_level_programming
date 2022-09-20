#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        test_list = [9, 20, 78, 100]
        self.assertEqual(max_integer(test_list), 100)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        test_list = [80, 56, 10, 60]
        self.assertEqual(max_integer(test_list), 80)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        test_list = [49, 37, 27, 19]
        self.assertEqual(max_integer(test_list), 49)

    def test_empty_list(self):
        """Test an empty list."""
        test_list = []
        self.assertEqual(max_integer(test_list), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        test_list = [60]
        self.assertEqual(max_integer(test_list), 60)

    def test_floats(self):
        """Test a list of floats."""
        test_list = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(test_list), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        test_list = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(test_list), 15.5)

    def test_string(self):
        """Test a string."""
        test_list = "random letters"
        self.assertEqual(max_integer(test_list), 's')

    def test_list_of_strings(self):
        """Test a list of strings."""
        test_list = ["test", "the", "string", "order"]
        self.assertEqual(max_integer(strings), "string")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
