# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = []

        def dfs(node):
            if not node:
                return
            
            array.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        array.sort()
        return array[k - 1]