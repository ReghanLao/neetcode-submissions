# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        
        #we will store a node's val here 
        self.path = [root.val]

        def dfs(node):
            #if we finish dfs traversal for a given path lets reset path (the root is in every path)
            if node is None:
                return 

            #is this node greater than all of the nodes we have seen so far in the path?
            if node.val >= max(self.path):
                self.count += 1

            self.path.append(node.val)

            dfs(node.left)
            dfs(node.right)

            self.path.pop()

        dfs(root)
        return self.count 
