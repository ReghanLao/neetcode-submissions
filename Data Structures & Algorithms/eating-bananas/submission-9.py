import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #try different rates 1 - k: if a given rate allows us to finish on time
        #how about we try another rate which is slower and see if it allows us to 
        #finish on time still or not 

        #using a BS to select the different rates 1 - k where k is 
        #the max rate we can eat at to finish all piles 

        left = 1
        right = max(piles) 
        best_rate = max(piles)

        #for every tested rate see how much time is taken and if less than h
        #then it is valid. in that case lets try a slower rate after 
        while left <= right:
            mid = (left + right) // 2
            curr_rate = mid
            time_taken = 0 

            for i in range(0, len(piles)):
                time_taken += math.ceil(piles[i] / curr_rate)
            
            #try to find a more minimum rate that could be better
            if time_taken <= h:
                best_rate = min(best_rate, curr_rate)
                right = mid - 1
            else:
            #we ate too slow so find a bigger rate 
                left = mid + 1


        return best_rate 

        
