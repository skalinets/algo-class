from unittest import TestCase

__author__ = 'serhiyk'

# Write a function, `count`
# that returns the units of time
# where each print statement is one unit of time
# and each evaluation of range also takes one unit of time

def count(n):
    # Your code here to count the units of time
    # it takes to execute clique
    min_count = 2
    inner_range_count = n
    inner_print_count = sum(range(n))
    result = min_count + inner_print_count + inner_range_count
    return result

def clique(n):
    print "in a clique..."
    for j in range(n):
        for i in range(j):
            print i, "is friends with", j

class Tester(TestCase):
    def test_should_return_2_for_0(self):
        self.assertEqual(2, count(0))

    def test_should_return_3_for_1(self):
        self.assertEqual(3, count(1))

    def test_should_return_3_for_2(self):
        self.assertEqual(5, count(2))
        
    def test_should_return_12_for_4(self):
        self.assertEqual(12, count(4))



    pass