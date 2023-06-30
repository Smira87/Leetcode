from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root:
            if root.left:
                output += self.inorderTraversal(root.left)
            output.append(root.val)
            if root.right:
                output += self.inorderTraversal(root.right)
        return output