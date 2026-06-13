# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #global variable in a sense (for this particular instance of a class the class will have a diameter of ...)
        self.diameter = 0 

        def dfs(node):
            #Base case:

            #we want to start building the solution starting at the leaf nodes of this tree
            #the path that can be formed at this leaf node to its children is len 0
            if node is None:
                return 0 
            
            #Recursive case:
            left = dfs(node.left)
            right = dfs(node.right)

            #the len of path at this particular node is just left + right
            #check if we can update our diameter of all time
            self.diameter = max(self.diameter, left + right)

            #the left of path that can be formed at this node and sent back to caller is 
            #max(left, right) + 1
            return max(left, right) + 1
        dfs(root)

        return self.diameter

        

