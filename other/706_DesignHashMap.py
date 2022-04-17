class LLNode:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.head = LLNode(key=-1, val=-1)

    def put(self, key: int, value: int) -> None:
        curnode = self.head
        while(curnode and curnode.next):
            if curnode.key == key:
                curnode.val = value
                return
            curnode = curnode.next
        if curnode.key == key: curnode.val = value
        else: curnode.next = LLNode(key=key, val=value)


    def get(self, key: int) -> int:
        curnode = self.head
        while(curnode):
            if curnode.key == key: return curnode.val
            curnode = curnode.next
        return -1

    def remove(self, key: int) -> None:
        curnode = self.head
        while(curnode and curnode.next):
            if curnode.next.key == key:
                nextnode = curnode.next.next
                curnode.next = nextnode
            curnode = curnode.next

"""---------------------------------------------------- Mod Hash Array ---------------------------------------------------------------"""
class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # better to be a prime number, less collision
        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]


    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)