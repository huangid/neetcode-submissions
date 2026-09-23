"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque()
        if root:
            q.append(root)
        while q:
            for i in range(len(q) - 1, -1, -1):
                n = q.popleft()
                n.next = q[0] if i >= 1 else None
                if n.left and n.right:
                    q.append(n.left)
                    q.append(n.right)
        return root