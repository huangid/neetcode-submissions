# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque()
        q.append((root, root.val))
        good = 0
        while q:
            node, preVal = q.popleft()
            if node.val >= preVal:
                good += 1
            if node.left:
                q.append((node.left, max(node.val, preVal)))
            if node.right:
                q.append((node.right, max(node.val, preVal)))
        return good