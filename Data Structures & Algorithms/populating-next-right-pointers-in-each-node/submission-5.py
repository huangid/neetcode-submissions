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
        if not root:
            return root
        q = deque([root])
        while q:
            temp = None
            for i in range(len(q)):
                node = q.popleft()
                node.next = temp
                temp = node
                if node.left and node.right:
                    q.append(node.right)
                    q.append(node.left)
        return root