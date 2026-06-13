import heapq
from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #maintain a min heap of size k 
        #this will allow us to naturally contain the k largest elements
        #in the heap because the element with the lowest frequency atp
        #will naturally be evicted 
        #our TC overall improves since we only maintain a heap of size k
        #our core operation aka insert into heap only takes log(k)?

        #first lets count the elements and their frequency
        counts = Counter(nums)
        #create and maintain a heap of size k
        heap = []
        heapq.heapify(heap)

        #as we add elements, the elements with a lower count will naturally be evicted
        for key, val in counts.items():
            heapq.heappush(heap, (val, key))

            while len(heap) > k:
                heapq.heappop(heap)

        sol = []

        for item in heap:
            sol.append(item[1])

        return sol




