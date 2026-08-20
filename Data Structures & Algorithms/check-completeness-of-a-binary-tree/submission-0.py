# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        seen_none = False
        while q:
            node = q.popleft()
            if not node:
                seen_none = True
            else:
                if node and seen_none:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True


        