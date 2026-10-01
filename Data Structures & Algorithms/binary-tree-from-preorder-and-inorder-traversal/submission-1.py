# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        Optimization 1:
        instead of scanning inorder using .index() to find the mid point used to
        partition a root's left subtree and right subtree use a hashmap 
        
        Hashmap is used to map the values of inorder to the index at which they
        occur at so that when we select a root from pre order we can just access
        the hashmap to see where this root value occurs in inorder in O(1)
        '''

        inorder_map = {}

        for idx, num in enumerate(inorder):
            inorder_map[num] = idx
        
        '''
        Optimization 2:
        Instead of slicing arrays and passing them to recursively build the tree 
        we are going to use the original arrays and have them be bounded by 
        pre_start (where we start looking in preorder to take a node for the root
        of a given subtree), in_start (the beginning
        of in order portion), and in_end (end of in order portion)

        By doing this we tell recursive calls what portions of the original 
        arrays to look in and work with 
        '''
        def dfs(pre_start, in_start, in_end):
            if in_start > in_end:
                return None
            #the root val is the first val of preorder array
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            #the mid point used to identify left and right subtrees is mid
            mid = inorder_map[root_val]

            #calculate size of left partition - lets us know where to start
            #looking for a root in preorder 
            left = mid - in_start

            root.left = dfs(pre_start + 1, in_start, mid - 1)

            root.right = dfs(pre_start + 1 + left, mid + 1, in_end)

            return root 

        return dfs(0, 0, len(inorder) - 1)