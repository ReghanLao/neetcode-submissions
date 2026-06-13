"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = { None: None }

        curr = head

        #create mapping of old nodes to new nodes 
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        #construct new list
        curr = head 
        while curr:
            new_node = old_to_new[curr]
            new_node.next = old_to_new[curr.next]
            new_node.random = old_to_new[curr.random]
            curr = curr.next 
        
        #the old head maps to new head 
        return old_to_new[head]

        
