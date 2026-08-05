# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        s = []
        node = root
        num = 0
        while s or node:
            while node:
                s.append(node)
                node = node.left
            node = s.pop()
            num += 1
            if num == k:
                return node.val
            node = node.right


