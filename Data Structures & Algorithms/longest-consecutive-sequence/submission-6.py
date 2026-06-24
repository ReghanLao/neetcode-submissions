class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
            we can add all numbers to a set and check for the existence
            of a consecutive sequence starting at a given number

            since we want to find the longest consecutive sequence we want to 
            start checking for a consecutive sequence only if a given number 
            is the start of a sequence otherwise we are wasting time
        '''

        seen = set()

        for num in nums:
            seen.add(num)

        #we can have duplicate nums but that doesnt
        #affect the logic of a consecutive sequence  
        max_count = 0          
        for num in nums:
            curr_num = num
            #this number is not the start of a sequence so skip unnecessary work
            if curr_num - 1 in seen:
                continue 

            count = 1
            #while the sequence can be extended note that
            while curr_num + 1 in seen:
                count += 1
                curr_num = curr_num + 1
            max_count = max(max_count, count)
        
        return max_count 


