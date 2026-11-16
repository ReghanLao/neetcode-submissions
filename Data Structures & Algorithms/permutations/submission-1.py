class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
            
            for num in nums:
                #if we have selected this number to in our permutation we dont want to select it again
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        backtrack([])
        return res