'''
    Why do we need to be concerned about every n + m element accross m adds when 
    we only care about the kth largest element. 

    What we should be concerned about instead are the k largest elements in the 
    stream not every n + m element.

    Therefore we can use a min heap of size k as we add elements to the stream 
    we update our min heap to contain the k largest elements that represent the
    point in the stream that we are currently at 

    The minimum element of this min heap is the kth largest element aka the 
    smallest element amongst the k largest elements 
'''
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        #initialize our heap of size k to only care about the k largest elements
        #at any given point in time so that we are able to return the kth largest
        #in O(1) time
        for num in nums:
            heapq.heappush(self.heap, num)

            while len(self.heap) > k: 
                heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        #if the size of our heap ever exceeds k we need to pop the min element from heap because we only care about the k largest element and we need to retain the kth largest at the root of this heap 
        while len(self.heap) > self.k: 
            heapq.heappop(self.heap)
        
        return self.heap[0]
        
