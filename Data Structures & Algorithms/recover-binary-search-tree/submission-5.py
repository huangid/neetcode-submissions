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
        prev, first, second = None, None, None
        stack = []
        node = root
        pre = -1e9
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            n = stack.pop()
            if n.val < pre:
                if not first:
                    first = prev
                second = n
            pre = n.val
            prev = n
            node = n.right
        first.val, second.val = second.val, first.val