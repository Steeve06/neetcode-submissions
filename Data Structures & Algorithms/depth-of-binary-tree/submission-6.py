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

        count = 1
        maxCount = 1

        if root.left:
            count +=1
            self.maxDepth(root.left)
            maxCount = max(count, maxCount)

        if root.right:
            count +=1
            self.maxDepth(root.right)
            maxCount = max(count, maxCount)

        return maxCount