from unittest import TestCase
import math

__author__ = 'serhiyk'

def russian_rec(a, b):
    return 0 if a == 0 else 2 * russian_rec(a / 2, b) if a % 2 == 0 else b + 2 * russian_rec((a - 1) / 2, b)


def func(a):
    return 3 *math.floor(math.log(a, 2)) + 4


class Tester(TestCase):
    def test_1_and_1(self):
         self.assertEqual(1, russian_rec(1,1))

    def test_500000000_and_200000000(self):
         self.assertEqual(100000000000000000, russian_rec(500000000,200000000))

    def test_single(self):
        self.assertEqual(16, func(20))
        self.assertEqual(10, func(4))

    def test_my_numbers(self):
        theory = [(a, 1 if a == 0 else 4 if a < 2 else 7 if a < 4 else 10) for a in range(1, 6)]
        print theory
        for (a, t) in theory:
            print a, t
            self.assertEqual(t, func(a))
