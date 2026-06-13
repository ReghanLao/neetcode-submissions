# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BST Definition: 
# for a given node all nodes in the left subtree have smaller values 
# and all nodes in the right subtree have larger values

# traverse the BST to find the paths p and q are in while keeping track of their 
# common ancestor in the process
# the minute their paths diverse we know that they will cease to have a common ancestor if 
# we keep traversing so return with the LCA we have tracked so far
# also note if we reach a node which is either equal to our p or q node then this node is our LCA as well and we can return it
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #dfs will return the LCA
        def dfs(node, p, q):
            #if both nodes greater than curr then we go right 
            if p.val > node.val and q.val > node.val:
                return dfs(node.right, p, q)
            elif p.val < node.val and q.val < node.val:
                #if both nodes less than our curr then we go left
                return dfs(node.left, p, q)
            else:
                #this means that either we have landed on a p or q value or our path's diverge here aka this is our LCA
                return node
        
        return dfs(root, p, q)
