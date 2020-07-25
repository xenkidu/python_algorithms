class QuickFindUF:

    def __init__(self, file=None, n=None):
        if file is not None:
            file = open(file, 'r')
            n = int(file.readline())
            self.id = [i for i in range(n)]
            self.sz = [1] * n
            for line in file:
                p, q = map(int, line.split(' '))
                # if not uf.connected(p, q):
                self.union(p, q)
                # print(f'{p}, {q}')
            file.close()
        elif n is not None:
            self.id = [i for i in range(n)]
            self.sz = [1] * n
        else:
            raise AttributeError

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i != j:
            if self.sz[i] < self.sz[j]:
                self.id[i] = j
                self.sz[j] += self.sz[i]
            else:
                self.id[j] = i
                self.sz[i] += self.sz[j]

    def count(self):
        s = set()
        for p in self.id:
            s.add(p)
        return len(s)

    def root(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def get_id(self):
        return self.id



if __name__ == '__main__':
    import timeit

    # print(timeit.timeit(QuickFindUF('algs4-data/tinyUF.txt'), number=10000))

    # uf_test()

    uf = QuickFindUF('algs4-data/mediumUF.txt')
    print(uf.count())