# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque([(root, 0)])
        level = 0
        res = []
        sublist = []
        #run bfs 
        while queue:
            node = queue.popleft()

            if node[0].left:
                queue.append((node[0].left, node[1] + 1))
            if node[0].right:
                queue.append((node[0].right, node[1] + 1))
            
            #if level of popped node is not the same as curr level we finalize curr level sublist
            #update level to level of popped node
            if node[1] != level:
                res.append(sublist)
                level = node[1]
                sublist = [node[0].val]
            else:
                sublist.append(node[0].val)

        #append last sublist
        res.append(sublist)
        return res
            