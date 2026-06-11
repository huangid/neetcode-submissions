"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.m = {}
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        if head in self.m:
            return self.m[head]

        c = Node(head.val)
        self.m[head] = c
        newNext = self.copyRandomList(head.next)
        newRandom = self.m.get(head.random)
        c.next = self.copyRandomList(head.next)
        c.random = self.m.get(head.random)
        return c