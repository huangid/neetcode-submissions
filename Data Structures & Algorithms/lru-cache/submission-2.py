class Node:
    def __init__(self, key, val, next, prev):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.m = {}
        self.cap = capacity
        self.left = Node(0, 0, None, None)
        self.right = Node(0, 0, None, self.left)
        self.left.next = self.right

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        self.remove(self.m[key])
        self.insert(self.m[key])
        return self.m[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.remove(self.m[key])
        n = Node(key, value, None, None)
        self.insert(n)
        self.m[key] = n

    def insert(self, node):
        self.cap -= 1
        if self.cap < 0:
            lru = self.left.next
            self.left.next = lru.next
            lru.next.prev = self.left
            del self.m[lru.key]
            self.cap += 1
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node
    
    def remove(self, node):
        self.cap += 1
        node.prev.next = node.next
        node.next.prev = node.prev
        
