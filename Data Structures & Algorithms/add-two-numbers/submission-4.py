# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
            Overarching Idea:
            We sum digits left to right since digits are stored in reverse
            order 

            We should add numbers and also account for their carry 

            Approach:
            We can iterate through both of these lists in parallel 
            Add the digits on a given iteration
            Compute the carry if necessary
            Continue adding digits in parallel if applicable
            Else there is probably only one digit left to carry down or 
            sum with the carry 
            Or we need to carry the carry value down in case there are no 
            more digits to iterate through and a carry still exists 
        '''
        #D.next points to result list's head
        D = ListNode()
        #ptr for D that will iterate thru D and set its values
        ptr = D

        carry = 0 

        #we still have digits l1 and l2 to sum together, or carry down, or sum with carry or carry the carry value down 
        while l1 or l2 or carry != 0:
            l1_val = None
            l2_val = None

            if l1:
                l1_val = l1.val
            else:
                l1_val = 0 
            
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0 
            
            #safe addition - already set l1_val and l2_val 
            result = l1_val + l2_val + carry 

            if result > 9:
                carry = 1
                result = result % 10
            else: 
                carry = 0 
            
            ptr.next = ListNode(result)
            ptr = ptr.next

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next 

        return D.next