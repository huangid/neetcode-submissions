# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        good = 0
        def dfs(node, premax):
            nonlocal good
            if node.val >= premax:
                good += 1
            if node.left:
                dfs(node.left, max(node.val, premax))
            if node.right:
                dfs(node.right, max(node.val, premax))

        dfs(root, root.val)
        return good