# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, diameter = 0):
        self.val = val
        self.left = left
        self.right = right
        self.diameter = 0

class Solution:
    def diameterOfBinaryTree(self, root):
        self.diametre = 0
        self.hauteur(root)         
        return self.diametre        

    def hauteur(self, root):
        if root is None:
            return 0
        left = self.hauteur(root.left)
        right = self.hauteur(root.right)
        self.diametre = max(self.diametre, left + right)
        return 1 + max(left, right)