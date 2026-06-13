import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums.copy()
        heapq.heapify(self.heap)

        #right now the heap has all elements in nums
        #we just need the k largest elements in the heap 
        #so we pop til the heap is of size k naturally pruning the smaller elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]
        
