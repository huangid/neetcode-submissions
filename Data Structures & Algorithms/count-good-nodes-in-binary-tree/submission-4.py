# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        s = []
        s.append((root, root.val))
        good = 0
        while s:
            node, premax = s.pop()
            if node.val >= premax:
                good += 1
            if node.left:
                s.append((node.left, max(node.val, premax)))
            if node.right:
                s.append((node.right, max(node.val, premax)))
        
        return good