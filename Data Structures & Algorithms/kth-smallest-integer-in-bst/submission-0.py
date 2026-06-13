# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #we know the smallest node is the left most node in the BST 
        #the kth smallest will be k - 1 steps away from this smallest node
        #we know that since the left branches represent the nodes which are smaller than
        #its parents we want to traverse all the way left and backtrack up in which
        #then we can say hey this is going to be our kth smallest node

        self.count = 0 
        self.res = root.val
        def dfs(node):
            if node is None:
                return 
            
            #after we are done traversing the smallest node branch then can we increment our count 
            dfs(node.left)
            self.count += 1
            print(self.count)
            print(node.val)
            if self.count == k:
                self.res = node.val
            dfs(node.right)
        
        dfs(root)

        return self.res