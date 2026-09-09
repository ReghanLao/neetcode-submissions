class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            Conventional Tabulation Approach 

            dp[i] represents the maximal amount of money we can make 
            following the rules when we start robbing from house 0 to i

            our base cases are dp[0] = nums[0] and dp[1] = max(nums[0], nums[1])
            because at index 0 the max we can make from index 0 is nums[0]
            and at index 1 the max we can make from index 0 is max(nums[0],
            nums[1])

            at each step we decide to rob the current house or not because
            we are not allowed to rob adjacent houses 
                if we rob i we accumulate nums[i] and accumulated dp[i-2] aka
                the maximal amount of money we can make in the most recent non
                adjacent house

                if we don't rob i we choose to accumulate the maximal amount of 
                money we have been making so far aka the money stored in dp[i-1]
        '''
    
        n = len(nums)

        #only can rob 1st house
        if n == 1:
            return nums[0]
        
        #can only choose to rob 1st or 2nd house
        if n == 2:
            return max(nums[0], nums[1])
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            #rob: nums[i] + dp[i-2]
            #not rob: accumulate dp[i-1]
            #which one will yield more money max(rob, not rob)
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return dp[n-1]
