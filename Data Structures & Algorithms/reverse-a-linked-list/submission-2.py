# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
            The whole idea:
                1. Reverse the connection between every single node
                2. Once we reach the end we return the reference to that 
                node as the new beginning of the list 
        '''

        prev = None 
        ptr = head

        while ptr:
            nxt = ptr.next
            ptr.next = prev
            prev = ptr 
            ptr = nxt

        return prev

