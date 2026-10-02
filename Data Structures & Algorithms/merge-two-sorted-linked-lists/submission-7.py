# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #will be used to reference the head of the new list (D.next)
        D = ListNode()

        #will be used as a ptr to iterate throughout the new list that is being constructed
        curr = D

        ptr1 = list1
        ptr2 = list2
    
        #while both ptrs are non null we can continue our comparisions and construction from alternately taking from one list or the other
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                curr.next = ptr1
                curr = curr.next
                ptr1 = ptr1.next
            else:
                #when ptr2.val is less or they are the same lets take from ptr2
                curr.next = ptr2
                curr = curr.next
                ptr2 = ptr2.next 
        
        #at this point we may have exhausted list1 or list2 just append the remaining nodes of list1 or list2 directly as they are already sorted we don't have to worry about the new list being sorted improperly 
        if ptr1:
            curr.next = ptr1
        else:
            curr.next = ptr2 

        #references the head of the new LL 
        return D.next


