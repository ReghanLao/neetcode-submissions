class Solution:
    def climbStairs(self, n: int) -> int:
        '''
            The basic possibilities:
            There is only one way to take 1 step
            There are two ways to take 2 steps
               1: 
                => 1 step
               2:
                1 step => 1 step

                => 2 step

            If we work backwards lets say at n = 3 we notice the number of ways to get to 3 is the same as 1 and 2 combined we
            just add an increment of 1 or 2 (this is for every n that is not a base case)

                3:  
                    (same as 2 but we are adding an increment of 1 step so the number of ways tech dont change)

                    1 step => 1 step => 1 step 
                    2 step => 1 step
                    
                    (same as 1 but we are adding an increment of 2 step so the number of ways tech dont change)
                    1 step => 2 step
        '''
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [0] * n

        #base cases 
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n - 1]