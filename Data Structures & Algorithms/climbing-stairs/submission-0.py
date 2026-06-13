class Solution:
    def climbStairs(self, n: int) -> int:
        #can recursively tackle this?
        #can either climb 1 or 2 steps 

        memo = {1: 1, 2: 2}

        def dfs(n):
            if n in memo:
                return memo[n]
            #the sum of the previous n steps comprise n and we need to memoize this for efficient calculation
            memo[n] = dfs(n-2) + dfs(n-1)

            return memo[n]
        
        return dfs(n)