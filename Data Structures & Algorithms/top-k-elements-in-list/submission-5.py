import heapq 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq_dict = {}
        heap = []
        res = []

        for num in nums:
            num_freq_dict[num] = num_freq_dict.get(num, 0) + 1
        
        for key, value in num_freq_dict.items():
            heapq.heappush(heap, (value, key))
            
            while len(heap) > k:
                heapq.heappop(heap)
            
        #now we are left with the top k most frequent on the heap
        for value, key in heap:
            res.append(key)
        
        return res


