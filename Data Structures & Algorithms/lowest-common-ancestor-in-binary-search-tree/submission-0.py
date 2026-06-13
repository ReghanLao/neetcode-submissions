# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #traverse the tree using props of a BST
        #if the nodes p and q are in different subtrees find the split at 
        #which this occurs this is our LCA because there is no common
        #ancestor below this split node in common to both p and q

        #starting at root because its is common to every node in tree
        curr = root

        #guaranteed to find sol and return (p and q both exist)
        while curr:
            #both p and q exist in right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            #both p and q exist in left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            #either a split occurs or one of p or q's values are equal to the current node
            #meaning this node is the LCA
            else:
                return curr
