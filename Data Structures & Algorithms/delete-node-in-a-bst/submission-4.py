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
                return
            if node.val > k:
                node.left = delete(node.left, k)
                return node
            elif node.val < k:
                node.right = delete(node.right, k)
                return node
            else:
                if not node.left:
                    node = node.right
                    return node
                else:
                    p = node.left
                    while p.right:
                        p = p.right
                    node.val = p.val
                    node.left = delete(node.left, p.val)
                    return node

        node = delete(root, key)
        return node

