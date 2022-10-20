from collections import deque

deq = deque()


class LRUCache:

    def __init__(self, limit=42):
        self.limit = limit
        self.dict_lru = {}
        self.deque_lru = deque()

    def get(self, key):
        if key in self.deque_lru:
            self.deque_lru.remove(key)
            self.deque_lru.append(key)
            return self.dict_lru[key]
        return None

    def set(self, key, value):
        self.deque_lru.append(key)
        if len(self.deque_lru) > self.limit:
            removed = self.deque_lru.popleft()
            del self.dict_lru[removed]
        self.dict_lru[key] = value
