# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def delete(node, k):
            if not node:
                return None
            if k > node.val:
                node.right = delete(node.right, k)
            elif k < node.val:
                node.left = delete(node.left, k)
            else:
                if not node.left:
                    return node.right
                n = node.left
                while n.right:
                    n = n.right
                node.val = n.val
                node.left = delete(node.left, n.val)
            return node
        root = delete(root, key)
        return root