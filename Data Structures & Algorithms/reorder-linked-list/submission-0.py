# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #split the LL into two halves using slow and fast ptr
        #once fast ptr hits the end then the slow will end up at middle
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #slow will now mark the middle so the second half starts after it
        second = slow.next 
        #severe first from second to form the halves
        slow.next = None 
        #reverse second half of list 
        prev = None 

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp 
        
        #now we have reversed the second half's links so we can go 
        #ahead and merge the two to reorder the LL while we have nodes to
        #weave together (take from second) half as it is the bottle neck
        #the head of the second half once reversed points to prev as second
        #becomes null from the reversal process 
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next 
            first.next = second 
            second.next = temp1 
            
            first = temp1
            second = temp2 

