class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
            Recursive Brute Force Solution 

            Try every possible sequence of coins and see which
            sequence will be minimum as we want the minimum sequence

            coins = [1,5,10], amount = 12

            We can start off choosing any of the available coins 
            1, 5, 10 and can continously select 1, 5, 10 again 
            and again 

            To see that we are getting closer to our amount we
            decrement from the total amount as we choose a coin
            and we account for the selected coin by doing a + 1 

            at every given point our recursive function dfs()
            holds the update amount we have to make total 
            dfs(total) lets say that this state represents the 
            minimum number of coins needed to make total
            so dfs will return the minimum number of coins which
            will make a given total 

            so lets say dfs(12) (min num of coins to make 12) depends
            on the min num of coins to make 11, 7, and 2

            thus each parent answer depends on the answer to the 
            subproblem the parent ultimately just adds 1 to what 
            ever the subprolem returns to account for the fact that
            we used the parent's coin

            Note however we have a lot of overlapping subproblems
            When drawing the recursive tree I saw that we need 
            to compute the minimum number of coins to make 2 more 
            than once.

            MEMO 

            Memo use a cache to map totals to computed min number of coins to make those totals
        '''

        #map base case total of 0 to being 0 coins needed minimally
        #total -> min ways to make total 
        memo = {0: 0}

        def dfs(total):
            #our subproblems will reduce total to 0 and when we have the edge case of amount being 0 at this point we can take 0 coins to make 0 
            if total == 0:
                return memo[0]
            #our subproblems can reduce total to less than zero in that case this current recursive sequence or sequence of coins cannot make amount - we don't want it to affect minimum so we should return some large infinite number as min(historical small num. inf) remains unaffected
            if total < 0:
                memo[total] = float('inf')
                return memo[total]

            #check if subproblem has been solved before 
            if total in memo:
                return memo[total]

            min_coins = float('inf')

            for coin in coins:
                #the min number of coins to make total is 1 + the min number of coins to make total - coin
                num_of_coins = 1 + dfs(total - coin)

                #the min number of coins required to make total is the min between historical min and the min number of coins to make total if the coin, coin was chosen
                min_coins = min(min_coins, num_of_coins)

            #we store the min number of coins to make total after it has been decided
            memo[total] = min_coins

            return memo[total]
        

        #if the min num of coins required is not inf then we have a valid sequence else there exist no valid sequence to make amount

        res = dfs(amount)
        if res == float('inf'):
            return -1
        else:
            return res