# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre = float('-inf')
        def check(t):
            nonlocal pre
            if t is None:
                return True
            if not check(t.left):
                return False
            if t.val <= pre:
                return False
            pre = t.val
            if not check(t.right):
                return False
            return True
        return check(root)
            