class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            At every given point besides the start we can choose to rob 
            this particular house at i but give up what we had accumulated 
            until i - 1 and just accumulate what was accumulated at i - 2

            IF we decide to not rob this house at i we just accumulate the 
            gains from i - 1 and move forward 

            We should decide between the max from nums[i] + nums[i-2] and
            nums[i-1]

            dp[i] represents the maximum amount of money we can rob up 
            until the ith house 
        '''
        n = len(nums)

        #if we only have one house to rob from
        if n == 1:
            return nums[0]
        
        #if we have two houses - the maximum between the first and two houses is the best choice
        if n == 2:
            return max(nums[0], nums[1])

        #else we can decide to rob the ith house but drop the funds accumulated through i - 1 and take the funds accumulated through i - 2 OR we can decide to not rob the ith house and accumulate the funds through i - 1

        dp = [0] * n 

        #the maximum amount of money we can make from the start is the starting amount
        dp[0] = nums[0]

        #the maximum amount of money we can make from one after the start is the maximum between the two starting houses because we can't select both the best choice is to take the maximum between them to rob 
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[n - 1]