# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #basically run a dfs and compute the sum of a given path from leaf to root
        #compare this sum against the target and return True if equal 

        #we only want to run the curr_sum check against target sum if we are at a leaf node
        self.flag = False
        self.curr_sum = 0 

        def dfs(node):
            if node is None:
                return 
            
            if node and (node.left is None and node.right is None):
                if self.curr_sum + node.val == targetSum:
                    self.flag = True

            self.curr_sum += node.val 
            dfs(node.left)
            dfs(node.right)
            #after we pop off node from stack we also need to remove its value from cumulative path sum 
            self.curr_sum -= node.val

        dfs(root)
        return self.flag