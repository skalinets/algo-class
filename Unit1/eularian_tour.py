from unittest import TestCase

__author__ = 'serhiyk'

# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def get_path(first, rest_nodes):
    if  not rest_nodes:
        return [first]

    candidates = []
    for g in rest_nodes:
        next = None
        if g[0] == first:
            next = g[1]
        elif g[1] == first:
            next = g[0]
        if next is not None:
            candidates.append((g, next))

    for n in candidates:
        g = rest_nodes[:]
        g.remove(n[0])
        np = get_path(n[1], g)
        if np:
            return [first] + np
    return []

def find_eulerian_tour(graph):
    # your code here
    
    ranks = {}
    for edge in graph:
        for e in edge:
            if e in ranks:
                ranks[e]  +=1
            else:
                ranks[e] = 1

    odd_nodes = [k for (k, v) in ranks.iteritems() if v % 2 == 1]
    first = odd_nodes[0] if odd_nodes else graph[0][0]

    return get_path(first, graph)

class Tester(TestCase):
    def test_should_return_result_for_3_nodes_edges(self):
        graph = [(1, 2), (2, 3), (3, 1)]
        result = find_eulerian_tour(graph)
        self.assertEqual([1, 2, 3, 1], result)

    def test_4_nodes_with_odd_start_finish(self):
        graph = [(1,2), (1,3), (2,3), (2, 4)]
        result = find_eulerian_tour(graph)
        self.assertEqual([2, 1, 3, 2, 4], result)


    def test_should_return_result_for_5_nodes(self):
        graph = [(1, 2), (2, 4), (3, 4), (5, 3), (1, 5)]
        expected = [1, 2, 4, 3, 5, 1]
        self.assertEqual(expected, find_eulerian_tour(graph))

    def test_testcase_2(self):
        graph = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
        expected = [0, 1, 7, 3, 6, 1, 5, 4, 8, 9, 5, 2, 4, 0]
        self.assertEqual(expected, find_eulerian_tour(graph))

    def test_testcase_3(self):
        graph = [(1, 13), (1, 6), (6, 11), (3, 13), (8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9), (1, 12), (4, 12), (5, 14), (0, 1), (2, 3), (4, 11), (6, 9), (7, 14), (10, 13)]
        expected = [1, 13, 3, 2, 6, 1, 12, 4, 11, 6, 10, 13, 8, 9, 5, 14, 7, 9, 6, 0, 1]
        self.assertEqual(expected, find_eulerian_tour(graph))

    def test_testcase_4(self):
        graph = [(8, 16), (8, 18), (16, 17), (18, 19), (3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14), (1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15), (6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]
        expected = [8, 16, 17, 3, 4, 12, 6, 5, 13, 17, 10, 1, 8, 18, 19, 2, 11, 14, 3, 18, 0, 1, 9, 7, 15, 13, 8]
        self.assertEqual(expected, find_eulerian_tour(graph))

    def test_some_more_graph(self):
        graph = [(0, 1), (1, 5), (4, 5), (5, 2), (5, 9), (8, 9), (4, 8), (4, 2), (4, 0) ]
        expected = [0, 1, 5, 4, 8, 9, 5, 2, 4, 0]
        self.assertEqual(expected, find_eulerian_tour(graph))