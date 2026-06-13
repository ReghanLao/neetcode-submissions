# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #will traverse the tree level order first so BFS
        #for every node that we visit we want to swap
        #its left and right child's positions 

        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            # process left and right nodes
            if node: 
                queue.append(node.left)
                queue.append(node.right)
                # swap left and right nodes 
                temp = node.left
                node.left = node.right 
                node.right = temp 
        return root 

