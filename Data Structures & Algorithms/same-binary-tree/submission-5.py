# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    Lets recursively break this problem down into sub problems

    If we know the starting two nodes are equal to each other all we need to 
    verify is that the left subtrees are equal to each other and the right subtrees
    are equal to each other 

    We recursively step through each pair of left and right subtrees and determine
    if both pair of nodes in each respective subtree are equal

    Our recursive base cases include when both nodes are 

    1. Both none - we have iterated thru the entire tree/subtree and we haven't found
    any violating condition so we propagate True back to the caller 

    2. One is none and One is NOT None - we have iterated thru these two subtrees and 
    found a node that violates the definition of structurally equivalent 

    2. Both are not none but have different values - we have iterated thru these two
    subtrees and found that these two nodes violate the deinition of being equivalent
    in a value sense 

    Since for the root node we are immediately informed whether equality was violated
    (assuming it wasnt) now we need to return whether or not equality was violated
    in either trees aka we need to check if both equality was satified in left and
    in right subtrees



'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p, q):
            if p is None and q is None:
                return True
            elif p and not q:
                return False
            elif q and not p:
                return False
            elif p.val != q.val:
                return False
            
            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)

            return left and right

        return dfs(p, q)