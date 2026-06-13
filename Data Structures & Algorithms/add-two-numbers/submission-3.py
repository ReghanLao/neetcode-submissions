# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        D = ListNode()
        curr = D
        while carry != 0 or l1 or l2:
            digit1 = 0
            digit2 = 0

            if l1:
                digit1 = l1.val
            
            if l2:
                digit2 = l2.val

            digit = (digit1 + digit2 + carry) % 10 
            carry = (digit1 + digit2 + carry) // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            curr.next = ListNode(digit)
            curr = curr.next 
        
        return D.next




