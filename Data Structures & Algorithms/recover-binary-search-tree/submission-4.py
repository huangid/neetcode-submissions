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
        stack = []
        node = root
        n1 = n2 = None
        prev = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if prev and node.val < prev.val:
                n2 = node
                if not n1:
                    n1 = prev
                else:
                    break
            prev = node
            node = node.right
        n1.val, n2.val = n2.val, n1.val
            

