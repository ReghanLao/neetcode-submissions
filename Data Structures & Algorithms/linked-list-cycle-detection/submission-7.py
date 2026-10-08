# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
            A cycle is present if you can revist a node at least once 
            
            One solution:
            Iterate through list store node references in a set and check set to see if node
            has been visited prior 

            Fast & Slow Ptr Solution:
            Have a slow ptr iterate through the list moving 1 at a time
            Have a fast ptr iterate through the list moving 2 at a time

            If fast and slow land on the same node then there is a cycle in the list 
            Else - we are able to reach the end of the list via a ptr then these ptrs will never intersect thus no cycle 
        '''

        slow = head
        fast = head

        #while either one is not null continue slow and 
        while slow and fast:
            slow = slow.next

            if fast.next is None:
                fast = None
            else:
                fast = fast.next.next

            if slow and fast and slow == fast:
                return True 
        
        #we are able to reach the end of the list via a ptr then these ptrs will never intersect thus no cycle 
        return False
