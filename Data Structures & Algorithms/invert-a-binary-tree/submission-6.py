# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
            we can run a recursive DFS given the root of the tree
            once we hit our base case, we return None back up to 
            whichever frame called us — often a leaf node's frame,
            since a leaf's children are None.            
            Once left and right for the given node is evaluated
            we can swap left and right
            then we propagate our current node and swapped subtree back to the caller
            we do this for every single node and its subtree as we move back up the recursive stack
        '''
        def dfs(node):
            #indicates we are done iterating thru the 
            #particular path we are going down 
            if node is None:
                return None 
            
            #the caller obtains the left and right subtree for the current node
            left = dfs(node.left)
            right = dfs(node.right)

            #caller swaps left and right subtree for current node
            node.right = left
            node.left = right 

            #propagate node & swapped subtree back to caller for future swaps
            return node

        return dfs(root)

        '''
        basically the tree is being modified in place and 
        the root of the tree never 
        has its reference change and in general
        no of the nodes in the original tree has their references
        change so its fine to return the original root
        '''