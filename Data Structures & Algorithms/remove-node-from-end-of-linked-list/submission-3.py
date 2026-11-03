# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        reverse LL -> remove -> reverse LL 
        '''

        #step 1 - reverse LL 
        prev = None 
        curr = head

        while curr:
            tmp = curr
            nxt = curr.next

            curr.next = prev

            curr = nxt
            prev = tmp
        
        new_head = prev

        #step 2 - disconnect node n - n nodes from the beginning   

        # special case when n is 1 we skip the first node and the new list starts at the second node 
        if n == 1:
            new_head = new_head.next 
        #general case when n is > 1 we simply remove node n by setting it's prev to its next 
        else:
            ptr = new_head
            prev = None 

            #marks the node we are on 
            i = 1
            
            while i <= n:
                nxt = ptr.next  


                if i == n:
                    prev.next = nxt
                    
                prev = ptr
                ptr = ptr.next
                
                i += 1
            

        
        #step 3 reverse again 
        prev = None 
        curr = new_head

        while curr:
            tmp = curr
            nxt = curr.next

            curr.next = prev

            curr = nxt
            prev = tmp

        new_head = prev

        return new_head