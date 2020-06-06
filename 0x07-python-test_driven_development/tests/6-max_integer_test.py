#!/usr/bin/python3
""" Unittest for max_integer """
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Defines class to test max integer """

    def test_not_a_list(self):
        """ String arguments in list case """
        self.assertEqual(max_integer(["a", "e", "i"]), "i")
        self.assertEqual(max_integer(("a", "e", "i")), "i")

    def test_number_list(self):
        """ Number list case """
        self.assertEqual(max_integer([-4, -2, -3]), -2)
        self.assertEqual(max_integer([9, 5, 6, 3]), 9)
        self.assertEqual(max_integer([-1, 4, -3, 2]), 4)
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)
        self.assertEqual(max_integer([2]), 2)

    def test_empty_list(self):
        """ Argument None in list case """
        self.assertEqual(max_integer([]), None)

#if __name__ == '__main__':
 #   unittest.main()