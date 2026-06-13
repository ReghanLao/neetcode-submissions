# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #are these subtrees the same?
        def dfs(p, q):
            #if they differ structurally
            if p and not q:
                return False
            if not p and q:
                return False
            
            #they don't differ structurally but their values differ
            if (p and q) and p.val != q.val:
                return False
            
            #last case is if p and q are both null in this case they aren't
            #invalid it just means we have finished iterating thru the subtree
            #and no false condiitons were met so we return True

            if not p and not q:
                return True

            #continue dfs on left and right subtree - but not both left and 
            #right need to be valid for this curr tree to be valid
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        return dfs(p,q)