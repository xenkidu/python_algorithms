class QuickFindUF:

    def __init__(self, n):
        self.arr = [i for i in range(n)]

    def connected(self, p, q):
        return self.arr[p] == self.arr[q]

    def union(self, p, q):
        if not self.connected(p, q):
            pid = self.arr[p]
            qid = self.arr[q]
            for i in range(len(self.arr)):
                if self.arr[i] == pid:
                    self.arr[i] = qid

    def find(self):
        pass

    def count(self):
        s = set()
        for p in self.arr:
            s.add(p)
        return len(s)


    def get_arr(self):
        return self.arr

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
