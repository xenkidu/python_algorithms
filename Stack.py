"""
Stack API

This implementation uses a singly-linked list.
"""
import unittest
from Node import Node


class Stack:
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

    def push(self, item):
        node = Node(item)
        node.next = self.first
        self.first = node
        self.sz += 1

    def pop(self):
        if not self.is_empty():
            value = self.first.val
            self.first = self.first.next
            self.sz -= 1
            return value
        else:
            raise IndexError

    def is_empty(self):
        return self.sz == 0

    def size(self):
        return self.sz


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.stack_empty = Stack()
        self.words = 'The big red fox'
        for w in self.words.split(' '):
            self.stack.push(w)

    def test_pop_all_items_from_list(self):
        self.assertEqual([self.stack.pop() for _ in range(self.stack.size())], list(reversed(self.words.split(' '))))
        self.assertEqual(self.stack.size(), 0)

    def test_stack_implements_iterator(self):
        self.assertEqual([w for w in self.stack], list(reversed(self.words.split(' '))))

    def test_cannot_pop_from_empty_list(self):
        with self.assertRaises(IndexError):
            self.stack_empty.pop()


if __name__ == "__main__":
    unittest.main()
