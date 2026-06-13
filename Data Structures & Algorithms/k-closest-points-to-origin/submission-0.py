import math 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def computeDistance(x,y):
            return math.sqrt((x - 0)**2 + (y - 0)**2)
        
        point_to_distance = {}

        for point in points:
            distance = computeDistance(point[0], point[1])
            point_tuple = (point[0], point[1])
            point_to_distance[point_tuple] = distance 
        
        #sort points by distance to origin 
        sorted_point_to_distance = sorted(point_to_distance.items(), key=lambda item:item[1])
        print(sorted_point_to_distance)

        res = []
        #retrieve the first k keys aka the first k points in sorted list
        for i in range(k):
            res.append(list(sorted_point_to_distance[i][0]))
        print(res)

        return res
