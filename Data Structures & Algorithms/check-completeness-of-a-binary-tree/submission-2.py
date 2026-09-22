# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        seen = False
        while q:
            node = q.popleft()
            if not node:
                seen = True
            if node:
                if seen:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True
