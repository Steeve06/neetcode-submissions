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

        count = 0
        maxCountl = 0
        maxCountr = 0

        if root.left:
            count +=1
            self.maxDepth(root.left)
            maxCountl = max(count, maxCountl)

        if root.right:
            count +=1
            self.maxDepth(root.right)
            maxCountr = max(count, maxCountr)

        return max(maxCountl,maxCountr) + 1