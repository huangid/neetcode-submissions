# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        side = []
        if not root:
            return []
        q = deque()
        q.append((root, 0))
        while q:
            node, h = q.popleft()
            if h == len(side):
                side.append(node.val)
            if node.right:
                q.append((node.right, h+1))
            if node.left:
                q.append((node.left, h+1))
        return side