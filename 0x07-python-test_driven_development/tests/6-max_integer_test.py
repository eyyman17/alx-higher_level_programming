#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ The Testing Class """

    def test_return(self):
        """ Testing the return of the function """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([-3, -5, -7]), -3)
        self.assertEqual(max_integer([17]), 17)
        self.assertEqual(max_integer([10, 3, 45, 99, 75]), 99)
