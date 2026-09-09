class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            For Tabulation Approach Intution + Details Refer to Collanote

            But for preface the essentials:

            1. We define dp[i] to be the maximal money we can rob starting from
            the ith house to the end going through non adjacent houses 

            2. Our base cases are similar to our recursive base cases
                a house exceeding n yields a gain of 0 
            
            3. To cover all possibilities for gain we can rob starting from
            house 0 or 1
        '''

        n = len(nums)
        dp = [0] * (n + 3)
        
        for i in range(n - 1, -1, -1):
            dp[i] = nums[i] + max(dp[i + 2], dp[i + 3])

        return max(dp[0], dp[1])