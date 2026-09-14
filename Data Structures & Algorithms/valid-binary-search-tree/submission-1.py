# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    In order for a node to be 'valid' aka part of a subtree rooted at parent x 

    If in left subtree:
    min <= node.val <= max where 
    min is the minimum value it has to be - inheritted from its parent 
    max is a value st its <= its parent's value 

    If in right subtree:
    min <= node.val <= max where 
    min is a value st its >= parent's value 
    max is the maximum value it has to be - inheritted from its parent 

    The immediate child's value depends on not only what the parent's value is 
    but also what bounds the parent
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_bound, max_bound):
            #able to iterate through subtree without running into issues therefore valid subtree
            if node is None:
                return True

            #test if node's val lies within the bound 

            if not(node.val > min_bound and node.val < max_bound): 
                return False
            
            #verify that left and right subtrees are valid 
            return dfs(node.left, min_bound, node.val) and dfs(node.right, node.val, max_bound)
        
        return dfs(root, float('-inf'), float('inf'))
        