# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        leftSize = self.size(root.left)
        if k == leftSize + 1:
            return root.val
        elif k <= leftSize:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - leftSize - 1)

    def size(self, root):
        if root is None:
            return 0
        return self.size(root.left) + self.size(root.right) + 1