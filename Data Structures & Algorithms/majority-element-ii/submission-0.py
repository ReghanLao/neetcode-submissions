from collections import Counter 

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_counts = Counter(nums)
        n = len(nums)
        res = set()

        for num in nums:
            #check if the count of this particular number is > n/3 
            if num_counts[num] > n/3:
                res.add(num)      
          
        return list(res)