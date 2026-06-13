class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)

        #i will keep track of purchase price
        for i in range(n):
        #j will keep track of selling price 
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)

        return max_profit 