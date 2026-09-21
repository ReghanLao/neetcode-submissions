# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
            Trees are equal if same structure and nodes share same value
            Trees are not equal if differ in structure or differ in value 

            Idea is to iterate through each of these trees in parallel and if 
            they ever differ in structure or value we return false

            Note the tree rooted at p and q to be equal so do their subtrees 
            so we need to check at all times whether or not p and q's left 
            and right subtrees are equal as well 

            1               
           2 3
          4 5

            1
           2 3
          4 6

          subtrees are not equal therefore entire tree is not equal 
        '''


        def dfs(p_node, q_node):
            #if able to iterate through both trees w/o issues valid
            if p_node is None and q_node is None:
                return True 
            
            #check for invalidation cases 
            if p_node and not q_node:
                return False
            elif q_node and not p_node:
                return False
            #they both exist but values differ
            elif q_node.val != p_node.val:
                return False
            
            #for the current node x are both the corresponding subtrees in both trees  equal?
            return dfs(p_node.left, q_node.left) and dfs(p_node.right, q_node.right)
        
        return dfs(p,q)