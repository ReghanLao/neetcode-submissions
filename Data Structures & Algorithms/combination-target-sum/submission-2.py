class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
            Since we are tasked with finding all combinations
            and our input is relatively small we can try to
            recursively backtrack to build 
            every single possible combination

            Our choices in recusively backtracking our way into 
            generating all possible combinations is:
            1. Take the current number and keep taking
            2. Skip the current number and move onto to the next

            We just repeat these choices at every given recursive call
        '''

        res = []

        def backtrack(curr, i):
            if i > len(nums) - 1 or sum(curr) > target:
                return 
            
            if sum(curr) == target:
                res.append(curr.copy())
                return 
            
            #continously taking the curr num 
            curr.append(nums[i])
            backtrack(curr, i)

            #we skip the curr num and move onto next
            curr.pop()
            backtrack(curr, i + 1)

        backtrack([], 0)
        return res