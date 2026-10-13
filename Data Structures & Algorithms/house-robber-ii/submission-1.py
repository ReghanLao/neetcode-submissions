class Solution:
    def rob(self, nums: list[int]) -> int:
        '''
            Since the first and last house are adjacent due to the circle structure we cannot rob both of them in the same night 

            Therefore if we rob 1 we can only rob up til n - 2
            If we rob 2 we can rob up til n - 1 

            We should see which yields more and that is our result 
        '''

        n = len(nums)

        #if we only one house we can only make the amount of money made from robbing that single house
        if n == 1:
            return nums[0]
        #if we only have two houses and sine we can't rob adjacent houses we can only pick 1
        if n == 2:
            return max(nums[0], nums[1])

        #house1 will store the amount of money we can rob starting from the range 1 to n - 2
        #house2 will store the amount of money we can rob starting from the range 2 to n - 1
        house1 = 0
        house2 = 0
        
        #dp[i] is the amount of money we can make up to house i if we were to start at house 0
        #the money we can make up to house 0 is nums[0]
        #the most amount of money we can make up to house 1 is the max between house 0 and house 1 
        dp = [0] * (n - 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        #calculate the amount that can be made starting from house1
        for i in range(2, n - 1):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        house1 = dp[-1]
        #calculate the amount that can be made starting from house2
        
        #dp[i] is the amount of money we can make up to house i if we were to start at house 1
        #the money we can make up to house 1 is nums[1]
        #the most amount of money we can make up to house 2 is the max between house 1 and house 2 
        dp = [0] * n
        dp[1] = nums[1]
        dp[2] = max(nums[1], nums[2])
        for i in range(3, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        house2 = dp[-1]
        
        return max(house1, house2)