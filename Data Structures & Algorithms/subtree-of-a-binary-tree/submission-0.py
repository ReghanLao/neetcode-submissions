# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not t:
            return True 

        #t is non null but s is 
        if not s:
            return False 
        
        #both non null so check if T is subtree of S 
        if self.sameTree(s, t):
            return True
        
        #we check left and right subtrees of s to see if T is a subtree in either
        return (self.isSubtree(s.left, t) or 
                self.isSubtree(s.right, t))

    def sameTree(self, s, t):
        #BASE CASE: null trees are the same trees
        if s is None and t is None:
            return True
        
        #if both are not null that means both can be iterated thru and have values checked
        #trees are equal if both their subtrees are equal - so we iterate thru
        #both their left and right subtrees and compare their sositions and evaluate their values at those sositions 
        if (s and t) and (s.val == t.val):
            return (self.sameTree(s.left, t.left) and 
            self.sameTree(s.right, t.right))

        #or one is null or values don't match
        #then they are not the same binary tree
        return False