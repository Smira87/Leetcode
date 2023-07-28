from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def height(node):
            if not node:
                return False
            return max(height(node.left), height(node.right)) + 1
        hl = height(root.left)
        hr = height(root.right)

        left_balanced = self.isBalanced(root.left)
        right_balanced = self.isBalanced(root.right)

        return abs(hl - hr) <= 1 and left_balanced and right_balanced

