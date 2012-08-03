__author__ = 'serhiyk'

import math
import unittest

def time(n):
    """ Return the number of steps
    necessary to calculate
    `print countdown(n)`"""
    minimum_steps = 3
    num_of_loops = 0
    x = n
    while n > 0:
        num_of_loops += 1
        n -= 5
    steps = minimum_steps + num_of_loops * 2
    # YOUR CODE HERE
    return steps

def countdown(x):
    y = 0
    while x > 0:
        x -= 5
        y += 1
    print y

#print time(50)

class Tests(unittest.TestCase):
    def test_should_return_3_for_0(self):
        self.assertEqual(3, time(0))

    def test_should_return_5_for_1(self):
        self.assertEqual(5, time(1))

    def test_should_return_5_for_2(self):
        self.assertEqual(5, time(2))

    def test_should_return_7_for_6(self):
        self.assertEqual(7, time(6))

    pass
