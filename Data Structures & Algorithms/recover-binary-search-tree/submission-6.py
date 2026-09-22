# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = n1 = n2 = None
        pVal = -1e9
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.val < pVal:
                if not n1:
                    n1 = prev
                n2 = node
            pVal = node.val
            prev = node
            node = node.right
        n1.val, n2.val = n2.val, n1.val

