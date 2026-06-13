class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(index, curr_sum, nums):
            if curr_sum == target:
                res.append(nums.copy())
                return
            
            if index >= len(candidates) or curr_sum > target:
                return 
            
            #choose candidates[index]
            curr_sum += candidates[index]
            nums.append(candidates[index])
            backtrack(index + 1, curr_sum, nums) 

            curr_sum -= candidates[index]
            nums.pop()
            #before branching ensure that next branch (same recursive level as prev) doesn't have the same value as this can cause dup combos
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index + 1, curr_sum, nums)
        backtrack(0, 0, [])
        return res