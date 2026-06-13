class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        longest = 0
        for num in nums:
            s.add(num)
        
        for num in s:
            if num - 1 not in s:
                #this number is a start of a sequence even if the sequence is of size 1
                curr_length = 1
                next_num = num + 1

                #checks for the presence of consecutive nums til there are no more which aka forms a consecutive sequence
                while next_num in s:
                    curr_length += 1
                    next_num += 1
                
                longest = max(longest, curr_length)
        
        return longest 