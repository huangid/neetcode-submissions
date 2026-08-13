# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}
        def dfs(node, rob):
            if not node:
                return 0
            if node not in cache:
                cache[node] = [None, None]
            if cache[node][rob] is not None:
                return cache[node][rob]
            
            if rob:
                cache[node][rob] = node.val + dfs(node.left, False) + dfs(node.right, False)
            else:
                cache[node][rob] = max(dfs(node.left, False), dfs(node.left, True)) + max(dfs(node.right, False), dfs(node.right, True))

            return cache[node][rob]
        return max(dfs(root, False), dfs(root, True))