from unittest import TestCase

__author__ = 'serhiyk'

def russian_rec(a, b):
    return 0 if a == 0 else 2 * russian_rec(a / 2, b) if a % 2 == 0 else b + 2 * russian_rec((a - 1) / 2, b)

class Tester(TestCase):
    def test_1_and_1(self):
         self.assertEqual(1, russian_rec(1,1))

    def test_500000000_and_200000000(self):
         self.assertEqual(100000000000000000, russian_rec(500000000,200000000))
