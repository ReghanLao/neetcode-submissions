import math 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = math.inf
        max_profit = 0

        for i in range(len(prices)):
            min_price = min(min_price, prices[i])

            profit = prices[i] - min_price

            max_profit = max(max_profit, profit)
        
        return max_profit