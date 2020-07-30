"""
This library contains algorithms for sorting.
"""
import unittest
from random import randint


class Selection:

    @staticmethod
    def sort(a):
        n = len(a)
        for i in range(n):
            min_ = i
            for j in range(i + 1, n):
                if a[j] < a[min_]:
                    min_ = j
            # exchange
            a[i], a[min_] = a[min_], a[i]
        return a


class TestSelection(unittest.TestCase):

    def test_selection_sorts_positive_integers(self):
        arr = [5, 1, 7, 99, 33, 13, 12, 11, 10, 10, 21, 19, 35]
        self.assertEqual(sorted(arr), Selection.sort(arr))

    def test_selection_sorts_random_integers(self):
        arr = [randint(-200, 200) for _ in range(100)]
        self.assertEqual(sorted(arr), Selection.sort(arr))


if __name__ == '__main__':
    unittest.main()
