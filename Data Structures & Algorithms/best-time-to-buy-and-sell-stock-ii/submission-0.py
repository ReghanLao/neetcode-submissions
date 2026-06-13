class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two ptrs: 
        #   left representing the buy date
        #   right representing the sell date (current price)

        left = 0
        profit = 0 

        for right in range(len(prices)):
            #how much profit can we make by selling today?
            if prices[right] - prices[left] > 0:
                #we have made profit add that to our total profit
                profit += prices[right] - prices[left]

                #once we have made a sale we can no longer hold a share at
                #the price listed on the left date

                #we can buy it again after sold it though at current price
                left = right 
            else:
                left = right 
        
        return profit 

