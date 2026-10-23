class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
            Bottom up DP 

            dp[i] - the minimum number of coins to make a total i 

            given 

            coins = [1,5,10], amount = 12

            and 

            dp = [0, x, x, x, x, x, x, x, x, x, x, x, x]

            our base case is when our total that we have to make is 0 in that
            case we use a minimum of 0 coins to make 0

            note when we cannot make a difference 
            coins = [2], amount = 3

            dp = [ 0, x, x, x ]

        '''

        # dp[i] - the minimum number of coins to make a total i 
        dp = [0] * (amount + 1)

        #the total number of coins to make 0 is 0 coins
        dp[0] = 0

        for i in range(1, amount + 1):
            #represents the mininum number of coins for each total i 
            min_coins = float('inf')

            #for the given total i try every coin to see which will yield a mininum number of coins overall used to make total i 
            for coin in coins: 
                #the amount of coins required is 1 to account for the current coin we are using plus the number of coins needed to make the difference 
                difference = i - coin

        
                #if we cannot make a difference its min number of coins is set to -1

                #if our difference is computed and it's impossible to make then we should skip 
                if difference >= 0 and dp[difference] != -1:
                    coins_required = 1 + dp[difference]
                    min_coins = min(min_coins, coins_required)
                else:
                    continue  
            
            if min_coins == float('inf'):
                dp[i] = -1
            else:
                dp[i] = min_coins 

        return dp[amount]
        

