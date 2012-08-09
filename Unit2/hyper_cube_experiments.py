from unittest import TestCase

__author__ = 'serhiyk'


#def get_

class Tester(TestCase):
    def test_that_1_xor_0_is_1(self):
        self.assertEqual(1, 1 ^ 0)

    def test_that_01_xor_10_is_11(self):
        self.assertEqual(0x11, 0x10 ^ 0x01)
