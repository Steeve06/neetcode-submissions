# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        listOfNodes = []

        if root:
            q.append(root)

        while q:
            nodePerLevel = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    nodePerLevel.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if nodePerLevel:
                listOfNodes.append(nodePerLevel)
        return listOfNodes
                