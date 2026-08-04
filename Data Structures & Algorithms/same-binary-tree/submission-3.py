# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    Two binary trees are equivalent if they share the same structure and each nodes 
    have the same value 

    Run BFS on both of these trees and add tree nodes to two seperate queues, p_queue 
    and q_queue

    Go through both queues and check for equality through popping

'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
 
        #bfs will return the queue contents after iterating through the tree rooted at Treenode 'node' 
        def bfs(node):
            res = [node]
            queue = [node]

            while queue:
                node = queue.pop(0)

                if node: 
                    left = node.left
                    right = node.right 

                    queue.append(left)
                    queue.append(right)

                    res.append(left)
                    res.append(right)
            
            return res


        p_queue = bfs(p)
        q_queue = bfs(q)
        
        #if one tree is shorter than the other they aren't equivalent
        if len(p_queue) != len(q_queue):
            return False

        while p_queue and q_queue:
            p_node = p_queue.pop(0)
            q_node = q_queue.pop(0)

            if p_node and not q_node:
                return False
            elif q_node and not p_node:
                return False
            elif (p_node and q_node) and (p_node.val != q_node.val):
                return False 
        
        return True
        
