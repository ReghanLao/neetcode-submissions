class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        #if we only one house we can only make the maount of money made from robbing that single house
        if n == 1:
            return nums[0]
        #if we only have two houses and sine we can't rob adjacent houses we can only pick 1
        if n == 2:
            return max(nums[0], nums[1])

        #house1 will store the amount of money we can rob starting from 1 to n - 2
        #house2 will store the amount of money we can rob starting from 2 to n - 1
        house1 = 0
        house2 = 0
        
        #for house1 the amount we can earn from the start is nums[0] and since we are starting from 1 what we would carry over at house 2 would be what we can make from house 1
        dp = [0] * (n - 1)
        dp[0] = nums[0]
        dp[1] = nums[0]

        #calculate the amount that can be made starting from house1
        for i in range(2, n - 1):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        house1 = dp[-1]
        #calculate the amount that can be made starting from house2
        
        #for house2 the amount we can earn from the start is nums[1] and since we are starting from 2 what we would carry over at house 3 would be the max between them since we are able to say choose house i and accumualte 2 and or not choose house i and accumulate 3 
        dp = [0] * n
        dp[1] = nums[1]
        dp[2] = max(nums[1], nums[2])
        for i in range(3, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        house2 = dp[-1]
        
        return max(house1, house2)