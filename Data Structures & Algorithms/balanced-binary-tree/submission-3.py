# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
            For every node determine if the height of the left and right subtree
            differ in height by more than 1, if so then we flag this 
            isn't a balanced Binary Tree 

            For this problem the recursive function will calculate the height
            and the flag will mark whether or not the tree is balanced 
        '''     

        self.balanced = True

        def dfs(node):
            #the height of a null node is 0 
            if node is None:
                return 0 
            
            #for a given node determine the left and right heights
            #the height at a given node is 1 + (to accomodate for the current node level) the previous heights accumulated in subproblems
            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)

            #for this node determine if its left and right subtree height differ by more than 1 
            if abs(left - right) > 1:
                self.balanced = False

            #caller needs to know the height to append to its height calculation -
            #naturally the caller would want to know the height of the max height
            #child as is the bottleneck 
            return max(left, right)

        dfs(root)
        return self.balanced
