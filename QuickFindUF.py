class QuickFindUF:

    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.sz = [1 for _ in range(n)]

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]

    def find(self):
        pass

    def count(self):
        s = set()
        for p in self.id:
            s.add(p)
        return len(s)

    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def get_id(self):
        return self.id

def qf_test():
    file = open('algs4-data/tinyUF.txt', 'r')
    N = int(file.readline())
    uf = QuickFindUF(N)
    for line in file:
        p, q = line.split(' ')
        p, q = int(p), int(q)
        if not uf.connected(p, q):
            uf.union(p, q)
    file.close()

if __name__ == '__main__':
    import timeit
    print(timeit.timeit(qf_test))

    file = open('algs4-data/tinyUF.txt', 'r')
    N = int(file.readline())
    uf = QuickFindUF(N)
    for line in file:
        p, q = line.split(' ')
        p, q = int(p), int(q)
        if not uf.connected(p, q):
            uf.union(p, q)
            print(f'{p} {q}')
    file.close()