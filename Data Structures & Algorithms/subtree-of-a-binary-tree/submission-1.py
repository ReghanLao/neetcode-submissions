# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#if we run a dfs on the og tree 
#we check at every single node in the og tree can this node produce
#a subtree is the same as subroot 
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p, q):
            #a tree is not the same tree if they don't have the same structure
            #or their values diff at a given node 

            if p and not q:
                return False
            if q and not p:
                return False

            if (p and q) and p.val != q.val:
                return False
            
            if not p and not q:
                return True 
            
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)
        
        self.flag = False
        def dfs(node):
            if node is None:
                return 
            
            if sameTree(node, subRoot):
                self.flag = True

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.flag
