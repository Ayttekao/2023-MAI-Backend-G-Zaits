import string

from lab_01.cache.Node import Node


class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        if capacity <= 0:
            raise ValueError("cache size must be greater than 0")
        else:
            self.capacity = capacity
            self.cache = {}
            self.head = Node()
            self.tail = Node()
            self.head.next = self.tail
            self.tail.prev = self.head

    def get(self, key: str) -> str:
        result: string

        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            result = node.value
        else:
            result = ""

        return result

    def set(self, key: str, value: str) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self._add(node)

        if len(self.cache) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.cache[node.key]

    def remove(self, key: str) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            del self.cache[key]

    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
