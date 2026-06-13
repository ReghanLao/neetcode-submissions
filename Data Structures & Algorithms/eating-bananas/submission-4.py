import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) 
        res = []

        #perform binary search mech on speeds to determine valid potential speeds
        while left <= right:
            speed = (left + right) // 2
            total_time = 0

            #will the speed here allow us to finish on time
            for pile in piles:
                total_time += math.ceil(pile / speed)
            

            if total_time <= h:
                #we can finish on time so lets look for slower speeds 
                res.append(speed)

                right = speed - 1
            else:
                # we need to look for faster speeds
                left = speed + 1

        return min(res)
            

