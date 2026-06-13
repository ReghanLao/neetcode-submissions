# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #run BFS simultaneously on both trees and check the nodes at the same 
        #current iterated over position - if the same then valid else not valid

        queue = deque([p,q])

        while queue:
            node_p = queue.popleft()
            node_q = queue.popleft()

            #if both nodes are none we don't enqueue anything as no neighbors for both nodes exist
            if node_p is None and node_q is None:
                continue 
            #if one of them are none, the other isnt so these trees are structurally not the same 
            if node_p is None or node_q is None:
                return False 
            #they are both non none then if their values are diff then also not the same binary tree
            if node_p.val != node_q.val:
                return False
            
            queue.append(node_p.left)
            queue.append(node_q.left)
            
            queue.append(node_p.right)
            queue.append(node_q.right)
        
        return True 