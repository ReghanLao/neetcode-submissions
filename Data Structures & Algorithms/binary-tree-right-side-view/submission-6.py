# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
            The question is asking us to return the rightmost node of every level
            in the tree 

            If we iterate through the tree using BFS and then iterate through
            every level of the tree we can then extract the last node in each
            level

            These nodes will be the nodes visible from the right side of the 
            tree 

            1 
           2 3 
          4  5

          level 0: [1] => [-1] => 1
          level 1: [2, 3] => [-1] => 3
          level 2: [4, 5] => [-1] => 5
        '''

        '''
        BFS - append nodes to a queue and process/visit them in the order they
        were appended
        BFS direction - left to right
        ''' 

        queue = deque()
        #iterate through the tree rooted at root using BFS 

        if root:
            queue.append(root)

        #stores values of every single last node on every level - right most nodes for every single level 
        res = []

        while queue: 
            #we want to store the nodes in a level collection to retrieve the last node in the current level in the end - so we need to process in level order
            #the queue at the beginning of each bfs iteration contains nodes on a particular level
            res.append(queue[-1].val)

            #we want to process all nodes on this level before moving to the next level 
            n = len(queue)

            for _ in range(n):
                curr = queue.popleft()
                
                #append left child to queue if possible
                if curr and curr.left:
                    queue.append(curr.left)

                #append right child to queue if possible
                if curr and curr.right:
                    queue.append(curr.right)

           
        return res




