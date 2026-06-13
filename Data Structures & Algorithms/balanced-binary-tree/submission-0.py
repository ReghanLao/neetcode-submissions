# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = True
        #obtain the heights of the left and right subtree thru recursive dfs
        #compare the heights if difference is greater than one return false else True
        def dfs(node):
            if node is None:
                return 0

            left_height = dfs(node.left) + 1
            right_height = dfs(node.right) + 1

            if abs(left_height - right_height) > 1:
                self.flag = False
            
            #return the height of which subtree? - max height
            return max(left_height, right_height) 
        dfs(root)
        #if dfs didn't return False then the tree is balanced 
        return self.flag
        

        
