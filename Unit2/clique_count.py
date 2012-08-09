from unittest import TestCase

__author__ = 'serhiyk'

#
# How many edges in a complete graph on n nodes?
#

def clique(n):
    # Return the number of edges
    # Try to use a mathematical formula...
    return ((n - 1) * n) >> 1


class Tester(TestCase):
    def test_that_1_returns_0(self):
        self.assertEqual(0, clique(1))

    def test_that_2_returns_1(self):
        self.assertEqual(1, clique(2))

    def test_that_3_returns_3(self):
        self.assertEqual(3, clique(3))

    def test_that_4_returns_6(self):
        self.assertEqual(6, clique(4))

    def test_that_5_returns_10(self):
        self.assertEqual(10, clique(5))
