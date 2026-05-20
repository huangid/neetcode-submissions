# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            n1, n2 = stack.pop()
            if n1 == None and n2 == None:
                continue
            if n1 == None or n2 == None or n1.val != n2.val:
                return False
            stack.append((n1.right, n2.right))
            stack.append((n1.left, n2.left))
        return True