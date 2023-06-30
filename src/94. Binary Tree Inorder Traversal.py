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