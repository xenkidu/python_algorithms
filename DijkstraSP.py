from EdgeWeightedDigraph import EdgeWeightedDigraph


class DijkstraSP:
    def __init__(self, G, s):
        """
        TODO: Get a working Priority Queue that implements decreasing an existing edge.
        """
        self.G = G
        self.start = s
        self.dist_to = [float('inf')] * G.V()
        self.edge_to = [None] * G.V()
        self.processed = [False] * G.V()

        self.dist_to[self.start] = 0.0

        for _ in range(G.V()-1):
            v = self.get_min()
            self.processed[v] = True
            self.relax(v)

    def relax(self, u):
        for edge in self.G.adj(u):
            v, w = edge.get_from(), edge.get_to()
            if self.dist_to[w] > self.dist_to[v] + edge.get_weight():
                self.dist_to[w] = self.dist_to[v] + edge.get_weight()
                self.edge_to[w] = edge

    def get_min(self):
        index = -1
        min_ = float('inf')
        for i, dist in enumerate(self.dist_to):
            if not self.processed[i] and dist < min_:
                min_ = dist
                index = i
        return index

    def get_dist_to(self):
        return self.dist_to

    def get_edge_to(self):
        return self.edge_to


if __name__ == '__main__':
    G = EdgeWeightedDigraph('./algs4-data/tinyEWD.txt')
    sp = DijkstraSP(G, 0)

