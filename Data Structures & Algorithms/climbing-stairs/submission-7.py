class Solution:
    def climbStairs(self, n: int) -> int:
        '''
            We want to reach the top nth step 

            We can climb with 
            1 step or 2 steps at a time 

            How many ways can we climb to the nth step given our base cases of 1 or 2 steps?

            How many ways can we reach the 1st step using our base cases
            => 1 step 

            How many ways can we reach the 2nd step using our base cases
            => 1 step => 1 step
            => 2 step

            How many ways can we reach the 3rd step using our base cases
            => 1 step => 1 step => 1 step
            => 1 step => 2 steps 
            => 2 step => 1 step 

            How many ways can we reach the 4th step using out base cases 
            => 1 step => 1 step => 1 step => 1 step
            => 1 step => 2 steps => 1 step  
            => 1 step => 1 step => 2 step
            => 2 step => 1 step => 1 step
            => 2 step => 2 step

            Notice that at every n step besides the base cases, we reuse the n - 1 step and 
            add just an incremental step to it 

            Note that at n = 3, we reuse n = 2 methods of steps 
            => 1 step => 1 step + increment of 1
            => 2 step + increment of 1

            The number of ways don't change an increment is just added 

            we also reuse the n-2 step and just add another increment step to it 
            => 1 step + increment of 1

            So we can say that the number of ways to get to the nth step is made possible
            or determined by reusing the n-1 number of ways and n-2 number of ways 

            # of steps to get to nth = # of steps to get to n-1 + # of steps to get to n - 2
        '''
        
        '''
            better approach: bottom up DP - tabulation 
        '''
        if n == 1:
            return 1 
        if n == 2:
            return 2 
        
        #each index starting from 1 represents the number of ways to reach that index'th step
        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 2 

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]