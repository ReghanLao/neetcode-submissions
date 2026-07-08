class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
            lets use a BS to determine the weight limit of the ship

            notice that once we don't need to go through every weight
            1. if the weight limit is too small - these weights will never give us the answer
            2. if the weight limit is very large - we should try lighter weight limits
        '''

        left = max(weights)
        right = sum(weights)

        while left < right:
            #this is the current weight we will assign to the ship
            curr = (left + right) // 2

            #this is the time it will take for us to ship at current weight
            days_taken = 0 

            #this is the load of the ship currently
            load = 0

            for weight in weights:
                if weight + load > curr:
                    days_taken += 1
                    load = weight 
                else:
                    load += weight 

            #if we do have a remaining yet to be shipped we need a day to ship it
            if load > 0:
                days_taken += 1

            if days_taken <= days:
                right = curr
            else:
                left = curr + 1
            
        #left and right will converge on one weight limit and that 
        #will be our answer
        return left 