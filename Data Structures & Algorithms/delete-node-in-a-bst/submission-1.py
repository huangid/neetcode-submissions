# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == key:
            if root.left is None and root.right is None:
                return None
            if root.left:
                node = root.left
                while node.right:
                    node = node.right
                root.val = node.val
                root.left = self.deleteNode(root.left, node.val)
            else:
                node = root.right
                while node.left:
                    node = node.left
                root.val = node.val
                root.right = self.deleteNode(root.right, node.val)
            return root
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root


    
        