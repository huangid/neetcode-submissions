# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque([root])
        tree = []
        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                leaf = queue.popleft()
                level.append(leaf.val)
                if leaf.left:
                    queue.append(leaf.left)
                if leaf.right:
                    queue.append(leaf.right)
            tree.append(level)
        return tree
