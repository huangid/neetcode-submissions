# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def f(r):
            if r is None:
                return
            t = self.height(r.left) + self.height(r.right)
            f(r.left)
            f(r.right)
            nonlocal diameter
            diameter = max(diameter, t)
        f(root)
        return diameter

    def height(self, tree):
        if tree is None:
            return 0
        return max(self.height(tree.left), self.height(tree.right)) + 1  
    