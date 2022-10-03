#!/usr/bin/pythone3
import unittest 
from models.square import Square 
import sys 
from io import StringIO 
import pep8 
from models.base import Base 
import json 
from models.rectangle import Rectangle 
import os 
""" 
This module contains all unittest for Base class 
""" 
  
  
class TestBase(unittest.TestCase): 
     """ 
     Class of functions to run tests 
     """ 
     def setUp(self): 
         """ 
         function to redirect stdout 
         """ 
         sys.stdout = StringIO() 
  
     def tearDown(self): 
         """ 
         cleans everything 
         """ 
         sys.stdout = sys.__stdout__ 
  
     def test_pep8_model(self): 
         """ 
         Tests for pep8 model 
         """ 
         p8 = pep8.StyleGuide(quiet=True) 
         p = p8.check_files(['models/base.py']) 
         self.assertEqual(p.total_errors, 0, "fix pep8") 
  
     def test_pep8_test(self): 
         """ 
         Tests for pep8 test 
         """ 
         p8 = pep8.StyleGuide(quiet=True) 
         p = p8.check_files(['tests/test_models/test_base.py']) 
         self.assertEqual(p.total_errors, 0, "fix pep8") 
  
     def test_docstrings(self): 
         self.assertIsNotNone(module_doc) 
         self.assertIsNotNone(Base.__doc__) 
         self.assertIs(hasattr(Base, "__init__"), True) 
         self.assertIsNotNone(Base.__init__.__doc__) 
         self.assertIs(hasattr(Base, "create"), True) 
         self.assertIsNotNone(Base.create.__doc__) 
         self.assertIs(hasattr(Base, "to_json_string"), True) 
         self.assertIsNotNone(Base.to_json_string.__doc__) 
         self.assertIs(hasattr(Base, "from_json_string"), True) 
         self.assertIsNotNone(Base.from_json_string.__doc__) 
         self.assertIs(hasattr(Base, "save_to_file"), True) 
         self.assertIsNotNone(Base.save_to_file.__doc__) 
         self.assertIs(hasattr(Base, "load_from_file"), True) 
         self.assertIsNotNone(Base.load_from_file.__doc__) 

    def test_none(self):
        """Testing when id is None"""
        base_1 = Base()
        base_2 = Base()
        base_3 = Base()

        self.assertEqual(base_1.id, 7)
        self.assertEqual(base_2.id, 8)
        self.assertEqual(base_3.id, 9)

    def test_id(self):
        """Testing when id is given"""
        base_1 = Base(12)
        base_2 = Base(13)
        base_3 = Base(14)

        self.assertEqual(base_1.id, 12)
        self.assertEqual(base_2.id, 13)
        self.assertEqual(base_3.id, 14)

    def test_for_both(self):
        """Testing for when id is given and id is None"""

        base_1 = Base()
        base_2 = Base(11)
        base_3 = Base()
        base_4 = Base(12)
        base_5 = Base()

        self.assertEqual(base_1.id, 1)
        self.assertEqual(base_2.id, 11)
        self.assertEqual(base_3.id, 2)
        self.assertEqual(base_4.id, 12)
        self.assertEqual(base_5.id, 3)

    def test_to_json_string(self):
        """Test to_json_string method"""
        r1 = Rectangle(10, 7, 2, 8)
        my_dict = r1.to_dictionary()
        my_str = '[{"x": 2, "y": 8, "height": 7, "width": 10, "id": 10}]'
        self.assertEqual(Base.to_json_string([my_dict]), my_str)
        self.assertEqual(Base.to_json_string(None), '[]')

        s1 = Square(10, 7, 2, 8)
        my_dict = s1.to_dictionary()
        my_str = '[{"id": 8, "x": 7, "size": 10, "y": 2}]'
        self.assertEqual(Base.to_json_string([my_dict]), my_str)

    def test_json(self):
        """Test JSON functionality"""
        r1 = Rectangle(10, 7, 2, 8)
        s1 = Square(10, 7, 2, 8)

        Rectangle.save_to_file([r1])
        Square.save_to_file([s1])

        r2 = Rectangle.load_from_file()
        r2 = r2[0]
        s2 = Square.load_from_file()
        s2 = s2[0]

        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.id, r2.id)
