import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
            To determine a rate we can select from the range
            min rate is 1 per hour always 
            max rate is the most amount of bananas in pile per hour 

            [min rate -> max rate]
            
            We can determine this rate linearly as our brute force
            implementation. Basically try every single possible rate
            from min to max and once we have found a rate st we can
            finish in time we return that rate 

            However, we don't need to try every single possible rate r
            
            We should only be trying rates that will get us closer 
            to our answer.
            
            Trying rates that will never get us to 
            finish on time should never have to be considered. 

            Thus we should run a BS on the range min rate to max rate
        '''

        min_rate = 1
        max_rate = max(piles)

        #run a BS on the valid possibe rates 
        #this eliminates 1/2 rates at every iteration that will
        #never lead to our answer 
        rate = 1

        while min_rate < max_rate:
            rate = (min_rate + max_rate) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / rate)

            #if this rate takes too much time 
            #we need to try a better rate - this means
            #discarding all rates slower than rate 
            if hours > h:
                min_rate = rate + 1 
            #we are able to finish on time lets try a slower rate
            #if possible - discard all greater rates than rate to try
            #slower rates 
            else:
                max_rate = rate

        return min_rate 
              


