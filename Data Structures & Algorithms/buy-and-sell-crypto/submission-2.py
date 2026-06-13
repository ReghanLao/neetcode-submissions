import math 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        right = 1
        n = len(prices)
    
        for right in range(n):
            if prices[right] < prices[left]:
                left = right
            
            profit = prices[right] - prices[left]

            max_profit = max(max_profit, profit)
        
        return max_profit 