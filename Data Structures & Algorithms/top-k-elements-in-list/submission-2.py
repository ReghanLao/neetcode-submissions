import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        heap = []
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [tup[1] for tup in heap]
        
