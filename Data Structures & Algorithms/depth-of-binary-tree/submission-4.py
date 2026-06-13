# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
#pre order traversal: Node -> Left -> Right 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        stack = [(root,1)]
        max_depth = -math.inf

        #our curr depth is always changing according to the node that was popped off the stack
        while stack:
            #visiting current node
            node = stack.pop()
            curr_depth = node[1]
            max_depth = max(max_depth, curr_depth)

            #marking its child nodes to be visited and updating their depth values
            if node[0].right:
                stack.append((node[0].right, node[1] + 1))
            
            if node[0].left:
                stack.append((node[0].left, node[1] + 1))
        
        return max_depth
            
        
        


