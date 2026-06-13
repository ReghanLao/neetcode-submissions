# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        right_side = []
        
        if root is None:
            return []
        #the nodes on the queue at the start of every single iteration are the nodes of a given level 
        #we want the last node of the given level because that node is the node visible on the right side 
        while queue:
            right_side.append(queue[-1].val)

            #iterate thru this level and continue bfs process
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                

        return right_side