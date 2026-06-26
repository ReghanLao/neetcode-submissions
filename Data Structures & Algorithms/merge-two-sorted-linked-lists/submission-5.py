# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2

        #dummy node will point to the head of the next list
        dummy = ListNode()
        curr = dummy
        print(dummy) 
        print(curr)
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                curr.next = ListNode(ptr1.val)
                ptr1 = ptr1.next 
            else:
                curr.next = ListNode(ptr2.val)
                ptr2 = ptr2.next 
            
            curr = curr.next 
        
        #when either ptr1 is exhausted we append the remaining elements in ptr2
        if ptr2:
            curr.next = ptr2 
        #the other case where ptr2 is exhausted
        if ptr1:
            curr.next = ptr1
        return dummy.next 


