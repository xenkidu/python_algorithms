# A class representing Directed Edges with Weights
class DirectedEdge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def __str__(self):
        return f'({self.v} -> {self.w}) {self.weight}'

    def get_weight(self):
        return self.weight

    def get_from(self):
        return self.v

    def get_to(self):
        return self.w
