"""
Bag API

Bag is implemented as a stack using a singly-linked list.
"""
import unittest


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class Bag:

    def __init__(self):
        self.first = None
        self.sz = 0

    def __iter__(self):
        self.iter = self.first
        return self

    def __next__(self):
        if self.iter is not None:
            result = self.iter.val
            self.iter = self.iter.next
            return result
        else:
            raise StopIteration

    def add(self, item):
        n = Node(item)
        n.next = self.first
        self.first = n
        self.sz += 1

    def is_empty(self):
        return self.first is None

    def size(self):
        return self.sz


class TestBag(unittest.TestCase):
    def setUp(self):
        self.bag0 = Bag()
        self.bag5 = Bag()
        self.bag25 = Bag()
        self.bag_of_words = Bag()
        self.words = "The big red fox"

        for n in range(1, 6):
            self.bag5.add(n)
        for n in range(1, 25):
            self.bag25.add(n)
        for word in self.words.split(' '):
            self.bag_of_words.add(word)

    def test_bag0_is_empty(self):
        self.assertTrue(self.bag0.is_empty())

    def test_bag5_has_5_items(self):
        self.assertEqual(self.bag5.size(), 5)

    def test_bag5_is_empty(self):
        self.assertFalse(self.bag5.is_empty())
        self.assertTrue(not self.bag5.is_empty())

    def test_bag5_implements_iterable(self):
        self.assertEqual([n for n in self.bag5], [5, 4, 3, 2, 1])

    def test_bag_of_words(self):
        self.assertEqual([w for w in self.bag_of_words], list(reversed(self.words.split(' '))))

if __name__ == "__main__":
    unittest.main(verbosity=2)
