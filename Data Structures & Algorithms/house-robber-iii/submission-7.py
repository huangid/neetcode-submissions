# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}
        def dfs(node):
            if node in cache:
                return cache[node]
            if not node:
                return [0, 0] # rob, not rob
            left = dfs(node.left)
            right = dfs(node.right)
            val1 = node.val + left[1] + right[1]
            val2 = max(left) + max(right)
            cache[node] = [val1, val2]
            return [val1, val2]

        return max(dfs(root))
            
                