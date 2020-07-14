from queue import PriorityQueue
from EdgeWeightedDigraph import EdgeWeightedDigraph


class DijkstraSP:
    def __init__(self, G, s):
        """
        TODO: Get a working Priority Queue that implements decreasing and existing edge.
        """
        self.distTo = [] * G.V()
        self.edgeTo = [] * G.V()
        self.pq = PriorityQueue()
        for v in range(G.V):
            self.distTo[v] = float('inf')
        self.distTo[s] = 0.0

        self.pq.put((s, self.distTo[s]))
        while not self.pq.empty():
            v = self.pq.get()
            self.relax(G, v)

    def relax(self, G, v):
        pass


if __name__ == '__main__':
    G = EdgeWeightedDigraph('./algs4-data/tinyEWD.txt')
    print(G)
