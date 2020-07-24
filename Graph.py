"""Graph API and graph related functions."""
import collections
import unittest


class Graph:
    """Create an empty graph with V vertices, or a graph from an input file."""

    def __init__(self, V=None, file=None):
        self.adj_list = collections.defaultdict(list)

        if file is not None:
            f = open(file, 'r')
            self.Vertices = int(f.readline())
            self.Edges = int(f.readline())
            for line in f.readlines():
                v, w = [int(u) for u in line.split(' ')]
                self.add_edge(v, w)
            f.close()
        elif V is not None:
            self.Vertices = V
        else:
            raise ValueError("No value was passed to constructor.")

    # adds edge (v,w)
    def add_edge(self, v, w):
        self.adj_list[v].append(w)
        self.adj_list[w].append(v)

    # returns vertices adjacent to v
    def adj(self, v):
        return self.adj_list[v]

    # number of vertices
    def V(self):
        return self.Vertices

    # number of edges
    def E(self):
        return self.Edges

    # string representation
    def __str__(self):
        pass


# compute the degree of vertex v
def degree(G, v):
    degree = 0
    for w in G.adj(v):
        degree += 1
    return degree


def max_degree(G):
    max_ = 0
    for v in range(G.V()):
        max_ = max(max_, degree(G, v))
    return max_


def average_degree(G):
    return 2 * G.E() / G.V()


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.G = Graph(file='./algs4-data/tinyG.txt')

    def test_create_graph_from_file(self):
        self.assertTrue(self.G.V() == 13)
        self.assertTrue(self.G.E() == 13)

    def test_degree(self):
        self.assertTrue(degree(self.G, 0) == 4)
        self.assertTrue(degree(self.G, 1) == 1)

    def test_max_degree(self):
        self.assertTrue(max_degree(self.G) == 4)

    def test_average_degree(self):
        self.assertTrue(average_degree(self.G) == 2.0)


if __name__ == '__main__':
    unittest.main()
