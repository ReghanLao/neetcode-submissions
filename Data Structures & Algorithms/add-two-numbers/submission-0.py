# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ""
        str2 = ""

        curr1 = l1
        curr2 = l2

        while curr1:
            str1 += str(curr1.val)
            curr1 = curr1.next
        
        while curr2:
            str2 += str(curr2.val)
            curr2 = curr2.next

        num1 = int(str1[::-1])
        num2 = int(str2[::-1])
        total = num1 + num2

        str_total = str(total)
        str_total = str_total[::-1]
        head = ListNode(int(str_total[0]))
        curr = head

        for i in range(1, len(str_total)):
            curr.next = ListNode(int(str_total[i]))
            curr = curr.next
        
        return head