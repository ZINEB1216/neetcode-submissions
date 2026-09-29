# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left = self.maxHeight(root.left)
        right = self.maxHeight(root.right)
        if abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right) :
            return True
        return False
    def maxHeight(self, root):
        if root is None:
            return 0
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))