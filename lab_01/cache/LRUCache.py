import string
from collections import deque


class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.__deque__ = deque(maxlen=capacity)
        self.__map___ = {}
        self.__cache_size__ = capacity

    def get(self, key: str) -> str:
        result: string

        try:
            self.__deque__.remove(key)
            self.__deque__.append(key)
            result = self.__map___[key]
        except ValueError:
            result = ""

        return result

    def set(self, key: str, value: str) -> None:
        if key not in self.__map___.keys():
            if len(self.__deque__) == self.__cache_size__:
                last = self.__deque__.pop()
                del self.__map___[last]
        else:
            self.remove(key)

        self.__deque__.append(key)
        self.__map___[key] = value

    def remove(self, key: str) -> None:
        self.__deque__.remove(key)
        del self.__map___[key]
