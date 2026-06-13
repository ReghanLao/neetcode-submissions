# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle of list - using fast and slow pointers
        slow = head 
        fast = head.next 

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
        
        second = slow.next 
        slow.next = None 

        #reverse the links of the second half
        prev = None 

        while second: 
            temp = second.next
            second.next = prev
            prev = second 
            second = temp 

        #now that we have reversed the second half we can go ahead and
        #start merging elements from their respective ends 

        second = prev 
        first = head
        while second:
            temp1 = first.next 
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1 
            second = temp2