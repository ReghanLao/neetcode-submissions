class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
            since our input size is relatively small we can 
            try generating every single possible combination

            since we want to generate every single possible combination
            this requires us to backtrack to undo a choice we made 

            in this case we are able to select a given number unlimited 
            times or choose another number - these are our choices

            after getting to a certain point and choosing an array of 
            numbers we can compute our sum and see if its our target

            if its our target this is part of the solution set 

            we run out of numbers to pick if we iterate through the array
            and we iterate out of bounds 
        '''
        res = []

        def backtrack(i, sol):
            if sum(sol) > target or i > len(nums) - 1:
                return 

            if sum(sol) == target:
                res.append(sol.copy())
                return 

            #select a number and continue selecting that number
            sol.append(nums[i])
            backtrack(i, sol)

            #don't select that number and select the next number
            sol.pop()
            backtrack(i + 1, sol)

        backtrack(0, [])
        return res