import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def computeDistance(x,y):
            return math.sqrt((x - 0)**2 + (y - 0)**2)

        max_heap = []

        #we will maintain a max heap of size k - this will allow us to 
        #consider only the k closest points to the origin as our answer
        #we don't care about all n points we just want to be left with the 
        #k closest points 

        for point in points:
            distance = computeDistance(point[0], point[1])

            heapq.heappush_max(max_heap, (distance, point))

            while len(max_heap) > k:
                heapq.heappop_max(max_heap)
        
        res = []

        for entry in max_heap:
            res.append(entry[1])

        return res