class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        left_count = self.maxDepth(root.right) + 1
        right_count = self.maxDepth(root.left) + 1

        return max(left_count, right_count)


sol = Solution()

#root = [3,9,20,null,null,15,7]

root = TreeNode(3)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


print(sol.maxDepth(root))