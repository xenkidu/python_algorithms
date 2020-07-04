class QuickFindUF:

    def __init__(self, n):
        self.id = [i for i in range(n)]

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        if not self.connected(p, q):
            i = self.root(p)
            j = self.root(q)
            self.id[i] = j

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

if __name__ == '__main__':
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
