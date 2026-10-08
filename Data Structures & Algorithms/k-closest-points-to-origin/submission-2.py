import math 
import heapq 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
            We want to calculate the distances from every point to the origin 
            and return the k closest points (the k points whose distances
            to the origin is minimized)

            Since we are only concerned about the k closests points to the origin
            aka the k points with minimal distance to the origin AFTER considering 
            ALL POINTS 

            We can store these k points with minimal distance on a MAX heap of size k st the
            heap is organized by distance. 

            After considering ALL points the max heap will contain the points that are
            minimal distance away from the origin BECAUSE all the points maximally away from
            the origin would have been popped

            Note:
            The answer is guaranteed to be unique so we cannot have duplicates in an answer
            meaning we dont have to worry about determining a way to break up ties in
            determining our ans
        '''

        #calculate the distance between a given point and origin 
        #x1,y1 = 0,0
        #x2, y2 = x,y
        def distance(x,y):
            return math.sqrt( (0-x)**2 + (0 - y)**2 )
        
        #will be a max heap organized by (distance, [coordinate])
        heap = []

        #will store the closest points to origin 
        res = []

        #calculate the distance b/w a point and origin and store on max heap 
        for point in points:
            dist = distance(point[0], point[1])

            heapq.heappush_max(heap, (dist, point))
            #since we are adding a node to the heap one at a time we just need a simple if 
            if len(heap) > k:
                heapq.heappop_max(heap)
        
        #the heap contains all out points of interest 
        for _, point in heap:
            res.append(point)

        return res

