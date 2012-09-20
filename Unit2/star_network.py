__author__ = 'serhiyk'

from unittest import TestCase

def star_network(n):
    # return number of edges
    return n - 1

class Tester(TestCase):
    def test_should_return_0_for_1(self):
        self.assertEqual(0, star_network(1))

    def test_should_return_1_for_2(self):
        self.assertEqual(1, star_network(2))

    def test_should_return_2_for_3(self):
        self.assertEqual(2, star_network(3))
        
    def test_should_return_5_for_6(self):
        self.assertEqual(5, star_network(6))

