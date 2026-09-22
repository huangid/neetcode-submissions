"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1 = p
        q1 = q
        while True:
            if p1 is q1:
                return p1
            p1 = p1.parent if p1.parent else p
            q1 = q1.parent if q1.parent else q