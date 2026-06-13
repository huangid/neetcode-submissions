# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        dep = 0
        def f(r, dep):
            if r is None:
                return
            if dep == len(res):
                res.append(r.val)
            f(r.right, dep+1)
            f(r.left, dep+1)
        f(root, dep)
        return res