from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        queue = deque([[root, 1]])

        while queue:

            node, level = queue.popleft()

            if node.left:
                queue.append([node.left, level + 1])
            if node.right:
                queue.append([node.right, level + 1])

        return level


sol = Solution()

#root = [3,9,20,null,null,15,7]

root = TreeNode(3)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(sol.maxDepth(root))