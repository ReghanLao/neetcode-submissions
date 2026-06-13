# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #BASE CASE: null trees are the same trees
        if p is None and q is None:
            return True
        
        #if both are not null that means both can be iterated thru and have values checked
        #trees are equal if both their subtrees are equal - so we iterate thru
        #both their left and right subtrees and compare their positions and evaluate their values at those positions 
        if (p and q) and (p.val == q.val):
            return (self.isSameTree(q.left, p.left) and 
            self.isSameTree(q.right, p.right))

        #or one is null or values don't match
        #then they are not the same binary tree
        return False