from collections import namedtuple

class LRUCache:

    def __init__(self, limit=42):
        self.limit = limit
        pass

    def get(self, key):
        pass

    def set(self, key, value):
        pass


cache = LRUCache(2)

cache.set("k1", "val1")
cache.set("k2", "val2")

print(cache.get("k3"))  # None
print(cache.get("k2"))  # "val2"
print(cache.get("k1"))  # "val1"

cache.set("k3", "val3")

print(cache.get("k3"))  # "val3"
print(cache.get("k2"))  # None
print(cache.get("k1"))  # "val1"

a = namedtuple()
a.s

# Если
# удобнее, get / set
# можно
# сделать
# по
# аналогии
# с
# dict:
# cache["k1"] = "val1"
# print(cache["k3"])