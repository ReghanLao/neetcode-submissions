class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []

        def backtrack(curr, i):
            if i == len(nums):
                sol.append(curr.copy())
                return
            
            curr.append(nums[i])
            backtrack(curr, i + 1)
            curr.pop()

            #we need to recurse as well with the case where we backtrack aka exclude
            backtrack(curr, i + 1)

        
        backtrack([], 0)
        return sol