# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(r):
            if r is None:
                return 0
            h1 = dfs(r.left)
            h2 = dfs(r.right)
            if h1 == -1:
                return -1
            if h2 == -1 or abs(h1-h2) > 1:
                return -1
            return max(h1, h2) + 1
        return dfs(root) != -1
