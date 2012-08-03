from unittest import TestCase

__author__ = 'serhiyk'

def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

def time(n):
    # The number of steps it takes to execute naive(a, b)
    # as a function of a
    return 3 + 2 * n

class Test(TestCase):
    def test_should_return_3_for_0(self):
        self.assertEqual(3, time(0))

    def test_should_return_5_for_1(self):
        self.assertEqual(5, time(1))

    def test_should_return_7_for_2(self):
        self.assertEqual(5, time(1))
