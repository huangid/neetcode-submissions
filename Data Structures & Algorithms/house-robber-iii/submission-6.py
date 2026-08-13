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
            val1 = node.val + dfs(node.left)[1] + dfs(node.right)[1]
            val2 = max(dfs(node.left)) + max(dfs(node.right))
            cache[node] = [val1, val2]
            return [val1, val2]

        return max(dfs(root))
            
                