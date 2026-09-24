class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
            Brute Force:
            Sort the array and for every position i check every i+1, i+2, ..., i + n position
            for consecutive elements and record the longest consecutive sequence this way

            Better Approach: 
            Instead of sorting and checking for consecutiveness using a nested approach we can ask ourselves for every element that we iterate through is there a consecutive sequence that starts at this element 

            for example 

            nums = [1,2,3]

            We know that at index 0, 1 is the start of a sequence and for every element for that matter is a start of a sequence right. 

            We want to ask are there elements that come after 1 that extends the sequence starting at 1 

            We need to know what comes after 1 right in the input so we need a way to keep track of this 
            
            in our case we can use a set to easily track all the numbers in the input and quickly check if there are elements after 1 in O(1) as existence operations in a set only take O(1) time

            We repeat this for every element.

            We can further optimize by only performing this check for elements that are 
            the start of the sequence because why would we ever want to check for the longest sequence at 2 or 3 if we know that it starts at 1. 
        """

        #records all elements in input so we have a record for consecutive element checking
        seen = set()

        for num in nums:
            seen.add(num)

        #stores the len of the longest consecutive sequence 
        res = 0

        for num in nums:
            #every number is inherently as start of sequence but we don't want to check the sequence starting at num if there is it's already part of another sequence because then this sequence starting at num will never be the longest sequence
            if num - 1 in seen:
                continue
            else:
                current_number = num
                seq_len = 1

                while current_number + 1 in seen:
                    seq_len += 1
                    current_number = current_number + 1
                
                res = max(res, seq_len)
        
        return res