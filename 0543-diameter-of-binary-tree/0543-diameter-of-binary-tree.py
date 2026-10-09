# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        diameter = self.depth(root.left) + self.depth(root.right)
        return max(diameter, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

    def depth(self, root: Optional[TreeNode]):
        if root == None:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
        