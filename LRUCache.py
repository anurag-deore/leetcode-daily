# https://leetcode.com/problems/lru-cache/
'''

DID NOT UNDERSTAND - REVISE

'''
from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.o = dict()
        self.deq = deque()

    def get(self, key: int) -> int:
        if key in self.o:
            val = self.o[key]
            self.deq.remove(key)
            self.deq.append(key)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if (key not in self.o):
            if(len(self.deq) == self.cap):
                d = self.deq.popleft()
                del self.o[d]
        else:
            self.deq.remove(key)
        self.o[key] = value
        self.deq.append(key)


# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
