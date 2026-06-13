class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                #that means num is the start of the sequence
                #now lets see how long this sequence is
                length = 1
                while num + 1 in nums_set:
                    length += 1
                    num = num + 1
                longest = max(length, longest)
        
        return longest 
