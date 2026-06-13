# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_len = 0
        curr = head

        while curr:
            list_len += 1
            curr = curr.next
        
        prev = None
        curr = head
        pos_to_del = list_len - n
        idx = 0

        #if we are trying to delete the head return head.next
        if n == list_len:
            return head.next 
        
        #we are deleting a non head node 
        while curr:
            if idx == pos_to_del:
                #perform deletion logic
                prev.next = curr.next
                curr.next = None
                #once we have deleted the node we don't need to iterate anymore
                break
            
            #move ptrs as we look for node to del
            prev = curr 
            curr = curr.next 
            idx += 1
        
        return head


