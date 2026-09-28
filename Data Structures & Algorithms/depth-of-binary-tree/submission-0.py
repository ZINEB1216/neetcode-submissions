# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        a = self.maxDepth(root.right)
        b = self.maxDepth(root.left)
        if a <= b:
            return 1+b
        else:
            return 1+a