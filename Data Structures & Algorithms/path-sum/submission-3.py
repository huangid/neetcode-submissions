# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(node, pathSum):
            curSum = pathSum + node.val
            if not node.left and not node.right and curSum == targetSum:
                return True
            check = False
            if node.left:
                check = check or dfs(node.left, curSum)
            if node.right:
                check = check or dfs(node.right, curSum)
            return check
        return dfs(root, 0)