# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #run bfs and create sub lists for each level
    
        queue = deque([root])
        res = []
        while queue:
            level = []

            #note that the queue only contains nodes from a given level 
            #at the start of each loop iteration naturally
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    level.append(node.val)
            if level:
                res.append(level)
        return res
