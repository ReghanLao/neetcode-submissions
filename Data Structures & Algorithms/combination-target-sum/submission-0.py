class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(index, curr_sum, curr_nums):
            if curr_sum == target:
                res.append(curr_nums.copy())
                return 
            
            #ensure we can only take from valid bounds and ensure we stop 
            #recursing if our curr_sum exceeds target to prevent unnecessary recursive calls
            if index >= len(nums) or curr_sum > target:
                return 
            
            #take number at index 
            curr_sum += nums[index]
            curr_nums.append(nums[index])
            backtrack(index, curr_sum, curr_nums)

            #don't take number at index
            curr_nums.pop()
            curr_sum -= nums[index]

            backtrack(index + 1, curr_sum, curr_nums)
        
        backtrack(0, 0, [])
        return res
