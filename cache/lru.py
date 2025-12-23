from collections import deque, OrderedDict

class Lru:
    def __init__(self, capacity: int = 3):
        self.cache = OrderedDict()
        self.capacity = capacity
    def put(self, key: str, data):
        if key not in self.cache and self.hasCacheFull():
            self.cache.popitem(True)
        self.cache[key] = data
        self.cache.move_to_end(key, last=False)
    def get(self, key: str):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key, last=False)
        return self.cache[key]
    def hasCacheFull(self):
        return len(self.cache) >= self.capacity

