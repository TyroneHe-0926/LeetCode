from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.length = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        try:
            value = self.cache[key]
            self.cache.move_to_end(key)
        except Exception:
            return -1
        return value
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return
        
        if len(self.cache) == self.length:
            for i in self.cache:
                del self.cache[i]
                break
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            self.cache[key] = value
            self.cache.move_to_end(key)


lRUCache = LRUCache(2);
lRUCache.put(2, 1)
lRUCache.put(1, 1)
lRUCache.put(2, 3)
lRUCache.put(4, 1)
print(lRUCache.get(1))
print(lRUCache.get(2))