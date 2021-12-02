
class DoubleLinkedNode:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity

        self.head, self.tail = DoubleLinkedNode(), DoubleLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeNode(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def addNode(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next = node
        node.next.prev = node

    def moveToFront(self, node):
        self.removeNode(node)
        self.addNode(node)

    def popTail(self):
        node = self.tail.prev
        self.tail.prev = node.prev
        self.tail.prev.next = self.tail
        return node


    def get(self, key):
        if key not in self.cache:
            return -1
        self.moveToFront(self.cache[key])
        return self.cache.get(key).value

    def put(self, key, value):

        node = self.cache.get(key)

        if not node:
            n = DoubleLinkedNode()
            n.key = key
            n.value = value

            self.cache[key] = n
            self.addNode(n)

            if len(self.cache) > self.capacity:
                del(self.cache[self.popTail().key])
        else:
            node.value = value
            self.moveToFront(node)


if __name__ == "__main__":
    print("hello world!")
    cache = LRUCache(2)
    cache.put(1, 10)

    cache.put(3, 33)

    cache.put(4, 22)

    cache.put(3, 11)

    print(cache.get(1))
    print(cache.get(3))
