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
            if node.val > k:
                node.left = delete(node.left, k)
            elif node.val < k:
                node.right = delete(node.right, k)
            else:
                if not node.right:
                    node = node.left
                else:
                    n = node.right
                    while n.left:
                        n = n.left
                    node.val = n.val
                    node.right = delete(node.right, n.val)
            return node
        deleteNode = delete(root, key)
        return deleteNode