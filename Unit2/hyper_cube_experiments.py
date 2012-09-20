from unittest import TestCase
import math

__author__ = 'serhiyk'

def bit_diff(p1, p2):
    p = p1 ^ p2
    c = 0
    while p > 0:
        if p % 2 == 1:
            c += 1
        p >>= 1
    return c


def get_cube_node_count(power):
    return int(math.pow(2, power))


def hypercube_edges(power):
    vertices = range(get_cube_node_count(power))
    n = 0
    for i in vertices[:-1]:
        for j in vertices[i:]:
            if bit_diff(i, j) == 1:
                n += 1
    return n

class Tester(TestCase):
    def test_that_1_xor_0_is_1(self):
        self.assertEqual(1, 1 ^ 0)

    def test_that_01_xor_10_is_11(self):
        self.assertEqual(0x11, 0x10 ^ 0x01)

    def test_that_110_and_010_has_one_bit_diff(self):
        self.assertEqual(1, bit_diff(0x110, 0x010))

    def test_that_1101_and_0100_has_one_bit_diff(self):
        self.assertEqual(2, bit_diff(0x1101, 0x0100))

    def test_that_1111_and_1111_has_one_bit_diff(self):
        self.assertEqual(0, bit_diff(0x1111, 0x1111))

    def test_that_2_hyper_cube_has_4_edges(self):
        self.assertEqual(4, hypercube_edges(2))
        
    def test_that_3_hyper_cube_has_12_edges(self):
        self.assertEqual(12, hypercube_edges(3))

    def test_that_4_hyper_cube_has_12_edges(self):
        self.assertEqual(12, hypercube_edges(3))

    def test_that_number_of_edges_prints(self):
        for i in range(2, 10):
            print get_cube_node_count(i), hypercube_edges(i)

