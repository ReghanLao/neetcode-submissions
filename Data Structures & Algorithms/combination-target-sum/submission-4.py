class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
            If the input size is small and we are asked to find 
            all combinations -> try every single possible combination
            and see if it sums to target via backtracking 

            Backtracking allows us to visit every single possible 
            combination of an input

            1. Choose 
            2. Recurse with option 1
            3. Undo 
            4. Recurse with other option 

            In this case our options are elements at index i 
            We advanced our index i to 
            i + 1 if we decide to undo and recurse with other option

            In other words option 1 is element at index i and 
            other option is element at index i + 1

            We stop exploring a given sequence if the total sum 
            is equal to our target or if it exceeds our target 

            When drawing the recursion tree we see that the 
            combinations we produce are unique so we are guaranteed 
            to be making and evaluating lists of unique combinations
            in each recursive call 

            They are unique because for every starting point we are 
            adding the same element that was previously used or adding
            a new element. Each recursion branch creates new combinations
        '''
        #stores unique combinations which sum to target
        res = []
        #candidate_list is the current combination
        #i is the position we can choose 
        #curr_sum represents the sum of the candidate_list
        def dfs(candidate_list, i, curr_sum):
            #found a combo
            if curr_sum == target:
                res.append(candidate_list.copy())
                return 
            
            #invalid sequence as numbers in combo can never reach target
            if curr_sum > target:
                return

            #our index passes all valid indicies
            if i > len(nums) - 1:
                return 
            
            #CHOOSE
            candidate_list.append(nums[i])
            curr_sum += nums[i]

            #RECURSE
            dfs(candidate_list, i, curr_sum)

            #UNDO
            num = candidate_list.pop()
            curr_sum -= num

            #Recurse Again - CHOOSE OTHER 
            dfs(candidate_list, i + 1, curr_sum)

        dfs([], 0, 0)

        return res
        

