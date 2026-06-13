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
        #pass one: we map old nodes to new nodes 

        #if curr.next is Null we should return Null
        mapping = {None: None}
        curr = head
        
        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next 
        
        #pass two: we leverage the mapping of old nodes to new nodes to allow 
        #new nodes to point to new nodes
        #we can access the old node's next and random ptr which map to corresponding 
        #old nodes, and since these old nodes map to new nodes we can link 
        #new nodes to new nodes 


        curr = head
        
        while curr:
            mapping[curr].next = mapping[curr.next]
            mapping[curr].random = mapping[curr.random]

            curr = curr.next
        
        return mapping[head]
