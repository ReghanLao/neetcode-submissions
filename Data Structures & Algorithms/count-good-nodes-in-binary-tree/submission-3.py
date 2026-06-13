# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #we can run a dfs starting from the root node and from there
        #as we go down the curr recursive path
        #we are able to pass on the value of the node of the greatest value so far
        #and we can compare that node's value with our curr node's value
        #if our curr node's value is greater than or equal to the passed down
        #node's value then this node is a good node and we have a new greatest node val for the curr path as well 

        self.count = 0 

        def dfs(node, greatest):
            if node is None:
                return 
            
            if node.val >= greatest:
                self.count += 1

            greatest = max(greatest, node.val)

            dfs(node.left, greatest)
            dfs(node.right, greatest)
        
        dfs(root, root.val)
        return self.count 
