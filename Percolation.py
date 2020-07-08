'''
The following class models a percolation system.
'''

class Percolation():
    # // creates n-by-n grid, with all sites initially blocked
    # public Percolation(int n)
    def __init__(self, n):
        self.grid = [[0] * n for _ in range(n)]

    # // opens the site (row, col) if it is not open already
    # public void open(int row, int col)
    def open(self, row, col):
        pass

    # // is the site (row, col) open?
    # public boolean isOpen(int row, int col)
    def is_open(self, row, col):
        pass

    # // is the site (row, col) full?
    # public boolean isFull(int row, int col)
    def is_full(self, row, col):
        pass

    # // returns the number of open sites
    # public int numberOfOpenSites()
    def number_of_open_sites(self):
        pass

    # // does the system percolate?
    # public boolean percolates()
    def percolates(self):
        pass

    # // test client (optional)
    # public static void main(String[] args)
    def test_client(self, args):
        pass