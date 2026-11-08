# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        '''
        Constraints:
        Tree can be empty 
        Key might not exist in tree so we return tree as usual
        10,000 nodes in tree
        '''

        if not root:
            return None 
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and root.right:
                return root.right
            elif not root.right and root.left:
                return root.left
            elif root.right and root.left:
                #traverse current node's right subtree and extract smallest aka leftmost in right subtree
                curr = root.right

                while curr.left:
                    curr = curr.left
                
                #val is in curr
                root.val = curr.val 
                root.right = self.deleteNode(root.right, curr.val)
            else:
                return None 
        return root 
