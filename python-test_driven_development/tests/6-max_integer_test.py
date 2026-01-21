#!/usr/bin/python3
"""Unittests for max_integer([..])"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer"""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -5, -20, -1]), -1)

    def test_mix_positive_negative(self):
        self.assertEqual(max_integer([-1, 0, 5, 3]), 5)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 9, 2, 3]), 9)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([1, 9, 2, 9, 3]), 9)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.9]), 2.7)

    def test_ints_and_floats(self):
        self.assertEqual(max_integer([1, 2.5, 3, 0.2]), 3)

    def test_default_argument(self):
        self.assertIsNone(max_integer())
