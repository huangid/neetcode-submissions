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
        copy = {None:None}
        def copyList(node):
            if node in copy:
                return copy[node]
            copyNode = Node(node.val)
            copy[node] = copyNode
            copyList(node.next)
            copyNode.next = copy[node.next]
            copyNode.random = copy[node.random]
        copyList(head)
        return copy[head]