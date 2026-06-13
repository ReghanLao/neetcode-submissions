# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0 
        curr_depth = 0
        stack = []

        if root:
            stack = [(root, 1)]

        while stack: 
            node = stack.pop(-1)
            curr_depth = node[1]
            print(curr_depth)
            max_depth = max(curr_depth, max_depth)

            if node[0] and node[0].right:
                stack.append((node[0].right, curr_depth + 1))
            if node[0] and node[0].left:
                stack.append((node[0].left, curr_depth + 1))

        return max_depth