# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2
        aux_arr = []

        while current1:
            aux_arr.append(current1.val)
            current1 = current1.next

        while current2:
            aux_arr.append(current2.val)
            current2 = current2.next

        aux_arr.sort()

        def ArrToLinkedList(arr):
            if not arr:
                return None
                
            head = ListNode(arr[0], None)
            current = head

            for i in range(1, len(arr)):
                current.next = ListNode(arr[i])
                current = current.next
            
            return head
        
        return ArrToLinkedList(aux_arr)


