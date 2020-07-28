"""
The class SP implements Shortest Path algorithms for an Edge-Weighted Digraph.
"""

from DijkstraSP import DijkstraSP
from EdgeWeightedDigraph import EdgeWeightedDigraph

class SP:

    def __init__(self, graph, s):
        self.graph = graph
        self.s = s
        self.dsp = DijkstraSP(self.graph, self.s)

    def dist_to(self, v):
        return self.dsp.dist_to[v]

    def path_to(self, v):
        stack = []
        edge = self.dsp.edge_to[v]
        while edge is not None:
            stack.append(edge)
            edge = self.dsp.edge_to[edge.get_from()]

        return stack

    def results(self):
        for v in range(self.graph.V()):
            print(f'{self.s} to {v} ({self.dsp.dist_to[v]:.3})', end=":\t")
            for e in self.path_to(v):
                print(e, end=" ")
            print()


if __name__ == '__main__':
    G = EdgeWeightedDigraph('./algs4-data/tinyEWD.txt')
    shortest_path = SP(G, 0)
    shortest_path.results()