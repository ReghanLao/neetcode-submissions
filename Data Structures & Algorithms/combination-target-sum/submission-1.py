class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, curr):
            if sum(curr) > target or i > len(nums) - 1:
                return 

            if sum(curr) == target:
                res.append(curr.copy())
                return

            #take 
            curr.append(nums[i])
            #take again
            backtrack(i, curr)

            #or move onto the next and don't take 
            curr.pop()
            backtrack(i + 1, curr)
            
        backtrack(0, [])
        return res