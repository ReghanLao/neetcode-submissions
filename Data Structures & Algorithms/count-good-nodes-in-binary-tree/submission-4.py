# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    We can iterate through the tree using DFS
    
    Keep track of the current local maximum for the current path we are on as we
    iterate through the tree

    If the current node is greater than the maximum in the path we have been
    walking through then this node is good
'''

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0 

        #node: the current TreeNode node we are iterating through
        #path_max: the local maximum in the path we are iterating through
        def dfs(node, path_max):
            if node is None:
                return 
            
            if node.val >= path_max:
                self.count += 1
            
            dfs(node.left, max(path_max, node.val))
            dfs(node.right, max(path_max, node.val))

        #init: our path_max will be -inf by default to start 
        dfs(root, float('-inf'))     
        return self.count 