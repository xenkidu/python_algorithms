import collections
from DirectedEdge import DirectedEdge
from Bag import Bag

class EdgeWeightedDigraph:
    def __init__(self, file):
        f = open(file, 'r')
        self.Vertices = int(f.readline())
        self.Edges = int(f.readline())
        self.adj_list = collections.defaultdict(list)
        for line in f:
            v, w, weight = line.split(' ')
            v, w, weight = int(v), int(w), float(weight)
            edge = DirectedEdge(v, w, weight)
            self.adj_list[v].append(edge)

    def V(self):
        return self.Vertices

    def E(self):
        return self.Edges

    def adj(self, v):
        return self.adj_list[v]

    def __str__(self):
        s = f'Vertices: {self.Vertices}\n' \
            f'Edges: {self.Edges}\n'
        for v in self.adj_list:
            for edge in self.adj_list[v]:
                s += str(edge) + '\n'
        return s
