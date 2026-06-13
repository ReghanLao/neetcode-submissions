from collections import Counter 
import heapq 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count the frequencies of all nums
        occur = Counter(nums)
        heap = []
        #go through every one of the num:frequencies and insert into the heap
        #if the size of the heap exceeds size k then pop the root so that
        #we always have the top k frequenet elements in the heap
        for num, freq in occur.items():
            heapq.heappush(heap, (freq,num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        #at the very end we are left with all top k frequent elements on the heap naturally
        for freq, num in heap:
            res.append(num)
        return res 
            

