# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
            Run a DFS from the root node down to every single 
            leaf node and compute the best possible depth aka the 
            maximum possible depth from root to leaf 
        '''

        #by having variables tied to the specific instance of this class
        #we are able to persist the curr depth at a given level and keep
        #track of it regardless of what branch we are on 
        self.max_depth = 0 
        self.curr_depth = 0

        def dfs(node):
            #we have finished traversing a path from root to leaf
            if node is None:
                self.max_depth = max(self.max_depth, self.curr_depth)
                return 

            #increments the current depth of the path we are on
            #if we arrive at a new level
            self.curr_depth += 1

            dfs(node.left)
            dfs(node.right)

            #backtrack and decrement current depth as we go back up a level
            self.curr_depth -= 1
        dfs(root)
        return self.max_depth 