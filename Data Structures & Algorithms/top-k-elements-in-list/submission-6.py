import heapq 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        res = []

        for num in nums:
            counts[num] += 1
        
        heap = []

        for key, val in counts.items():
            heapq.heappush(heap, (val, key))
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        for item in heap:
            res.append(item[1])
        
        return res