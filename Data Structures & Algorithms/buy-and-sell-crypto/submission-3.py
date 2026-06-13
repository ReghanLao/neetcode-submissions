class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0 
        sell = 1
        max_profit = 0
        n = len(prices)

        for sell in range(n):
            if prices[sell] < prices[buy]:
                buy = sell
            
            profit = prices[sell] - prices[buy]

            max_profit = max(max_profit, profit)
        

        
        return max_profit 