class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            Problem Overview
            We know that as a robber we cannot rob the adjacent house (i + 1) when 
            we are on i 

            Intuition:
            This leaves us with exploring and robbing the non adjacent houses from
            the ith house aka

            i + 2 house 
            i + 3 house 

            Why i + 2 and i + 3?
            
            If we step up in an increment of 2 or 3 from i we are inevitably bound 
            in visiting every possible non adjacent house - every non adjacent
            increment of 2 and every non adjacent increment of 3 covers all even
            and odd parity non adjacent houses
            
            If we had houses 1, 2, 3, 4, 5, 6

            (all possible non adjacent houses starting from 1)
            1 -> 3 -> 5
            1 -> 4 

            (all possible non adjacent houses starting from 2)
            2 -> 4 -> 6
            2 -> 5

            i + 2 and i + 3 explores all possibilities which are not adjacent to i
            when we start at i = 0 and i = 1 

            when deciding to rob the i+2 house or i+3 house explore how much 
            money we can make from both and take the maximal toward our
            accumulated money 

            Recurrence Relation:
            So our recurrence relation should naturally look like this (tracking
            maximum amount of money robber can rob)

            nums[i] + max(dfs(i + 2), dfs(i + 3))

            Examples:
            lets run through some examples
               0 1 2 3 4 5

            1.[1,1,3,3]
            3.[2,9,8,3,6,100]

            1. 
            f(0) -> f(2) and f(3)
                f(2) returns 3 
                f(3) returns 3
                Therefore f(0) = cost[0] + max(3,3) = 4
            f(2) -> f(4) and f(5) 
                f(4) returns 0 since out of bounds
                f(5) returns 0 
            f(3) -> f(5) and f(6) 
                f(5) returns 0 
                f(6) returns 0 

            3. 
            f(0) -> f(2) and f(3)
            f(2) -> f(4) and f(5)
            f(3) -> f(5) and f(6) <- f(5) recomputed here 
            ...

            Insights:
            We have repeated computations in example 3. for example f(5) is 
            recomputed multiple times when it can be cached 

            A better approach is to cache computed values so we only have to 
            calculate the maximum money we make when robbing house i once 
            instead of recalculating this when we encounter it again in the
            recursion tree 

            This reduces our time from 2^n to n since we only calculate once
            the amount of money we make from robbing the ith house at 
            most n times since our input is of size n 
        '''
        memo = {}
        def dfs(i):
            if i >= len(nums):
                return 0 
            
            if i in memo:
                return memo[i]

            memo[i] = nums[i] + max(dfs(i + 2), dfs(i + 3))
            
            return memo[i]
        
        return max(dfs(0), dfs(1))
