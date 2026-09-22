"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        m = {None:None}
        def copy(node):
            if not node:
                return None
            m[node] = Node(node.val)
            m[node].next = copy(node.next)
            m[node].random = m[node.random]
            return m[node]
        copy(head)
        return m[head]