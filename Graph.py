class Graph:

    def __init__(self, V=None, file=None):
        if file is not None:
            pass
        elif V is not None:
            pass
        else:
            raise ValueError("No value was passed to constructor.")

    def add_edge(self, v, w):
        # adds edge (v,w)
        pass

    def adj(self, v):
        # returns vertices adjacent to v
        pass

    def V(self):
        # number of vertices
        pass

    def E(self):
        # number of edges
        pass

    def __str__(self):
        # string representation
        pass


if __name__ == '__main__':
    pass
