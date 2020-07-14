# A class representing Directed Edges with Weights
class DirectedEdge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def __str__(self):
        return f'({self.v}, {self.w}) {self.weight}'

    def weight(self):
        return self.weight

    def v(self):
        return self.v

    def w(self):
        return self.w
