# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #search for the position that val should be inserted in (it can be inserted as a leaf node and then insert it there)

        #make sure original tree ties back to this new node 

        def dfs(node):
            #if we have found a place for val after BST traversal insert it here and connect it back to it'd parent's left or right subtrees
            if node is None:
                return TreeNode(val)
            if val > node.val:
                node.right = dfs(node.right)
            else:
                node.left = dfs(node.left)

            return node
        
        if root is None:
            return TreeNode(val)

        dfs(root)

        return root