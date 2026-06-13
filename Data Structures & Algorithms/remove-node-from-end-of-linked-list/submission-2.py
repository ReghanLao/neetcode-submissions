# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        list_len = 0

        while curr:
            list_len += 1
            curr = curr.next
        
        #node we are deleting is head 
        if list_len == n:
            return head.next 
        
        curr = head
        prev = None
        pos = 0 #lets make list 0 indexed
       
        while curr:
            if pos == list_len - n:
                #delete this node
                prev.next = curr.next 
                curr.next = None
            
            prev = curr
            curr = curr.next
            pos += 1
        
        return head 

