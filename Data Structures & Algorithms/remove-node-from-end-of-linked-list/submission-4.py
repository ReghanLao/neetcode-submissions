# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Using a slow and past ptr we maintain a gap of size n + 1 so that slow lands on the node before the node we want to remove allowing for ease of removal of target node

        The gap allows us to ensure our slow pointer will always land one right before target

        The Dummy node allows us to have our slow ptr start n + 1 positions from fast
        '''
        D = ListNode(0, head)
        slow = D
        fast = head 

        for _ in range(n):
            fast = fast.next

        # a gap of n + 1 exists between slow and fast now
        # advance both til slow lands on node right before target 
        # aka this happens when fast goes out of bounds since our gap naturally allows for the above to happen as fast goes out of bounds

        while fast: 
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return D.next