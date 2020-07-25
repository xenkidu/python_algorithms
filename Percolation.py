"""
The following class models a percolation system.
"""
from QuickFindUF import QuickFindUF
import unittest
from random import randint


class Percolation:
    # Creates n-by-n grid, with all sites initially blocked.
    def __init__(self, n):
        self.grid = [[0] * n for _ in range(n)]
        self.open_sites = 0
        self.uf = QuickFindUF(n=n ** 2 + 2)
        self.top = n ** 2
        self.bottom = n ** 2 + 1
        self.n = n
        # algorithm:
        # while system does not percolate, generate random site and open
        # after opening a site, check 4 surrounding neighbors
        # if a neighbor is open, connect the current site with neighbor

    # opens the site (row, col) if it is not open already
    def open(self, row, col):
        if self.is_open(row, col) is False:
            self.grid[row][col] = 1
            self.open_sites += 1
            # if row is top or bottom, we connect it to self.top, self.bottom respectively.
            site = self.point_to_id(row, col)
            if row == 0:
                self.uf.union(self.top, site)
            if row == self.n - 1:
                self.uf.union(self.bottom, site)

            # top neighbor:
            if row > 0 and self.is_open(row - 1, col):
                neighbor = self.point_to_id(row - 1, col)
                self.uf.union(neighbor, site)

            # bottom neighbor
            if row < self.n - 1 and self.is_open(row + 1, col):
                neighbor = self.point_to_id(row + 1, col)
                self.uf.union(neighbor, site)

            # left neighbor
            if col > 0 and self.is_open(row, col - 1):
                neighbor = self.point_to_id(row, col - 1)
                self.uf.union(neighbor, site)

            # right neighbor
            if col < self.n - 1 and self.is_open(row, col + 1):
                neighbor = self.point_to_id(row, col + 1)
                self.uf.union(neighbor, site)

    # is the site (row, col) open?
    def is_open(self, row, col):
        return self.grid[row][col] == 1

    # is the site (row, col) full?
    def is_full(self, row, col):
        return self.grid[row][col] == 2

    # returns the number of open sites
    def number_of_open_sites(self):
        return self.open_sites

    # does the system percolate?
    def percolates(self):
        return self.uf.connected(self.top, self.bottom)

    def percolation_threshold(self):
        if self.percolates():
            return self.open_sites / self.n**2

    def point_to_id(self, row, col):
        return row * self.n + col

    # test client (optional)
    def run_simulation(self):
        while self.percolates() is False:
            row, col = randint(0, self.n-1), randint(0, self.n-1)
            self.open(row, col)

class TestPercolation(unittest.TestCase):

    def test_initialized_percolation(self):
        self.perc = Percolation(3)
        self.assertFalse(self.perc.percolates())

    def test_percolates_after_manually_opening(self):
        self.perc = Percolation(3)
        self.perc.open(0, 0)
        self.perc.open(1, 0)
        self.perc.open(2, 0)
        self.assertTrue(self.perc.percolates())
        self.assertTrue(self.perc.number_of_open_sites() == 3)

    def test_does_not_percolate_after_manually_opening(self):
        self.perc = Percolation(3)
        self.perc.open(0, 0)
        self.perc.open(1, 0)
        self.perc.open(2, 2)
        self.assertFalse(self.perc.percolates())

    def test_run_simulation(self):
        self.perc = Percolation(200)
        self.perc.run_simulation()
        self.assertTrue(self.perc.percolates())


if __name__ == '__main__':
    unittest.main()
