class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #to form subsets -> we can choose to take from current index or skip 
        #to avoid duplicates we can sort the input array and  
        nums.sort()
        res = []
        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return 
            
            #choice 1: take the number at i
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            #choice 2: not take the number at i
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res 
