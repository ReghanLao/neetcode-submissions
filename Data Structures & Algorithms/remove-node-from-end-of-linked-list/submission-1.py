# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        D = ListNode()
        D.next = head

        A = B = D

        #we want the ahead ptr to be n + 1 positions from 
        #the behind ptr initially aka gap of size n
        for i in range(n + 1):
            A = A.next
        
        #while A is valid lets move A and B equally to maintain that gap
        while A:
            A = A.next
            B = B.next
        
        #if A steps out of bounds then B is one before the node we need to delete
        B.next = B.next.next

        return D.next

        