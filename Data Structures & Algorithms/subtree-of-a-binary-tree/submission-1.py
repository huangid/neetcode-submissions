# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(n1, n2):
            if n1 is None or n2 is None:
                return n1 is n2
            return n1.val == n2.val and same(n1.left, n2.left) and same(n1.right, n2.right)
        
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if same(node, subRoot):
                return True
            node = node.right
        return False