class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
            Try every possible coin. Choose a coin and subtract its value
            from the current remaining amount. 

            Continue building sequences recursively. For the remaining
            amount, try every possible coin again.
            
            Find the shortest sequence. Compare the number of coins needed
            for each choice and keep the minimum.
            
            Stop at the base cases.
            - If the remaining amount is 0, we've made the amount exactly, so
            we need 0 additional coins.
            - If the remaining amount is negative, that path is invalid, so
            return infinity.
        '''

        #dfs(total) represents the minimum number of coins to make a given total. However since many subproblems are repeated across different calls we can cache the minimum number of coins to make a given total every time we calculate that 
        
        #to make a total of 0 you can use a minimum of 0 coins
        memo = {0:0}
        def dfs(total):
            if total == 0:
                return memo[0]
            
            #this combination results in no way to make the original amount
            if total < 0:
                memo[total] = float('inf')
                return memo[total]

            #before we calculate the min number of coins for a given total see if it's been cache 
            if total in memo:
                return memo[total]

            min_coins = float('inf')
            for coin in coins:
                ways = 1 + dfs(total - coin)
                min_coins = min(min_coins, ways)
            
            memo[total] = min_coins
            return min_coins

        res = dfs(amount)

        if res == float('inf'):
            return -1
        else:
            return res