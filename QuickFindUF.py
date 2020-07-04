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

    def get_arr(self):
        return self.arr

if __name__ == '__main__':
    qf = QuickFindUF(10)

    print(qf.connected(0,1))
    qf.union(3,6)
    qf.union(0,3)
    qf.union(1,6)
    print(qf.connected(0,1))
    print(qf.connected(0,6))
    print(qf.get_arr())
    qf.union(2,5)
    qf.union(8,9)
    qf.union(5,9)
    print(qf.get_arr())