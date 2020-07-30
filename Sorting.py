"""
This library contains algorithms for sorting.
"""
import timeit
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


class Insertion:

    @staticmethod
    def sort(a):
        for i in range(len(a)):
            for j in reversed(range(1, i + 1)):
                if a[j] < a[j - 1]:
                    a[j], a[j - 1] = a[j - 1], a[j]
                else:
                    break
        return a


class Merge:

    @staticmethod
    def __merge(a, aux, low, mid, hi):
        for k in range(low, hi + 1):
            aux[k] = a[k]

        i, j = low, mid + 1
        for k in range(low, hi + 1):
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j > hi:
                a[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]:
                a[k] = aux[j]
                j += 1
            else:
                a[k] = aux[i]
                i += 1

    @staticmethod
    def __sort(a, aux, low, hi):
        if hi <= low:
            return
        mid = low + (hi - low) // 2
        Merge.__sort(a, aux, low, mid)
        Merge.__sort(a, aux, mid + 1, hi)
        Merge.__merge(a, aux, low, mid, hi)

    @staticmethod
    def sort(a):
        aux = [None] * len(a)
        Merge.__sort(a, aux, 0, len(a) - 1)
        return a


class TestSelection(unittest.TestCase):

    def test_selection_sorts_positive_integers(self):
        arr = [5, 1, 7, 99, 33, 13, 12, 11, 10, 10, 21, 19, 35]
        self.assertEqual(sorted(arr), Selection.sort(arr))

    def test_selection_sorts_random_integers(self):
        arr = [randint(-200, 200) for _ in range(20)]
        self.assertEqual(sorted(arr), Selection.sort(arr))


class TestInsertion(unittest.TestCase):

    def test_insertion_sorts_positive_integers(self):
        arr = [5, 1, 7, 99, 33, 13, 12, 11, 10, 10, 21, 19, 35]
        self.assertEqual(sorted(arr), Insertion.sort(arr))

    def test_insertion_sorts_random_integers(self):
        arr = [randint(-200, 200) for _ in range(20)]
        self.assertEqual(sorted(arr), Insertion.sort(arr))


class TestMerge(unittest.TestCase):

    def test_merge_sorts_positive_integers(self):
        arr = [5, 1, 7, 99, 33, 13, 12, 11, 10, 10, 21, 19, 35]
        self.assertEqual(sorted(arr), Merge.sort(arr))

    def test_merge_sorts_random_integers(self):
        arr = [randint(-200, 200) for _ in range(20)]
        self.assertEqual(sorted(arr), Merge.sort(arr))


if __name__ == '__main__':
    unittest.main()
