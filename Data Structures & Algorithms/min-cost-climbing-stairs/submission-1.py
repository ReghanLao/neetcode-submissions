class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
            Recursive Solution 
        '''
        memo = {}
        def dfs(i):
            if i >= len(cost):
                return 0
            
            #if cache already computed the min cost from i to other floor then return it instead of recomputing else we recompute 
            if i in memo:
                return memo[i]

            #we want to minimize our cost to reach the top of the staircase so if taking an increment of 1 is cheaper we will do so and vice versa if taking an increment of 2 is cheaper we will do so 

            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]
        

        #we can either start at 0 or 1 we need the minimum cost between these two starts
        return min(dfs(0), dfs(1))