# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, maxVal):
            if node is None:
                return 

            #is this node greater than the max value of the current path if so then it is a good node
            if node.val >= maxVal:
                self.count += 1

            dfs(node.left, max(node.val, maxVal))
            dfs(node.right, max(node.val, maxVal))

        dfs(root, root.val)
        return self.count 