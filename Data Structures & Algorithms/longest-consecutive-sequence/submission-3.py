class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #used for reference in our consecutive sequence checks later 
        available_nums = set()

        for num in nums: 
            available_nums.add(num)

        #perform the consecutive sequence checks
        longest = 0
        seq = 1

        for i in range(len(nums)):
            num = nums[i]
            while num + 1 in available_nums:
                seq += 1
                num = num + 1
            
            longest = max(longest, seq)
            seq = 1
        
        return longest
        

        
