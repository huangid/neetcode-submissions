# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}
        def dfs(node, r):
            if not node:
                return 0
            if (node, r) in cache:
                return cache[(node, r)]
            rob1 = 0
            if r:
                rob1 = node.val + dfs(node.left, False) + dfs(node.right, False)
            rob2 = dfs(node.left, True) + dfs(node.right, True)
            cache[(node, r)] = max(rob1, rob2)
            return cache[(node, r)]
        return dfs(root, True)