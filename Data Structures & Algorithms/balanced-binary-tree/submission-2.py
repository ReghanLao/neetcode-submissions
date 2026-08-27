# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
            The problem states that the height of the left and right subtrees for every node
            need not to differ by more than one

            We can obtain the heights of the left and right subtree and calculate the 
            difference between them for every caller node

            If the difference is greater than 1 then this entire tree is not balanced. We should 
            record this and return this at the end 

            After this:

            We then want to continue propagating back up the recursion tree to continue 
            calculating the length of the left and right subtrees rooted at nodes that live in
            upper recursion branches
            
            We need to progate the height of the tallest subchild to the caller in the upper 
            recursion branches to use in its own height calculations as this is way to properly
            identify a parent subtree's overarching height

            The height being 1 + max(left_height, right_height) - adding one to account for the
            parent node's 
        '''

        self.res = True

        def dfs(node):
            if not node:
                return 0
        
            #left and right store the heights of the left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                self.res = False

            #each level increases the height of a subtree by 1 
            return 1 + max(left, right)

        dfs(root)
        return self.res 

        
        '''
        for caller:
        left = 1
        right = 3

        for 3:
        left = 2
        right = 0

        for 4:
        left = 1
        right = 0

        for 5:
        left = 0 
        right = 0 
        '''