# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
Algo + Thoughts: 

Run a DFS through this tree, 

For every single node calculate the height of the left and right subtrees 

Compare the heights left & right together if they are differing by more than 1 then
it ain't balanced 

For every single parent node when we are calculating the height of the entire tree
rooted at that node we factor in the child subtree with the largest height 

Coding Steps 
1. Base case check 
2. Get Left heights
3. Get Right heights
4. After Left & Right obtained compare and return False if necessary 
5. Return to caller the height of the largesst child so that the caller and correctly
compute its own height with the largest height child factored in 

*the height of any tree at a given node is ultimately dictated by the height of the 
largest height child thats why we propagate the largest height child back up 

'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True

        def dfs(node):
            if node is None:
                return 0 

            left = dfs(node.left)
            right = dfs(node.right)

            height_difference = abs(left - right)

            print(height_difference)
            if height_difference > 1:
                self.is_balanced = False 

            #propagate the height of this subtree (1 + the height of its max child) back to the caller so it can be used in future height difference comparisons 
            return 1 + max(left, right) 
               
        
        dfs(root)
        
        #we checked every single subtree rooted at every node and everything is balanced
        return self.is_balanced 