# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
            To calculate the diameter of the tree we need to get the
            maximum length path that can be formed in the tree

            We can run a DFS and once we hit our base case we return 0
            to our caller so we can begin computing the height of the
            subtree

            Once we have the heights of our left and right subtree
            we can compute the length of the path that runs thru this given node by adding them together 

            To continue the process we need to pass the height of this subtree back to the caller (max between the left and right subtree of the given node + 1)
        '''        
        self.diameter = 0

        def dfs(node):
            if node is None:
                return 0 
            
            left = dfs(node.left)
            right = dfs(node.right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)
        dfs(root)
        return self.diameter 