class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
            Dynamic Programming Botton Up - Iterative Approach
        '''

        '''
            We have been focusing on tackling the overarching problem and solving
            subproblems later to provide answers to our overarching problems 

            eg:

            cost = [1,2,3]
            *cost from 3 to the end and 4 to the end are 0 

            to get min cost from 0 to the end we need to know:
                about the costs from 1 to the end 
                about the costs from 2 to the end
            
            to get min cost from 1 to the end we need to know:
                about the costs from 2 to the end
                about the costs from 3 to the end

            We can tackle this by solving subproblems first

            eg:
            1. to get min cost from 2 to the end we need to know 
                cost at 2 plus the cost from 3 to the end
                cost at 2 plus the cost from 4 to the end

            2. now that we know the cost from 2 to the end, finding
            1 to the end is just 
                cost at 1 plus the cost from 2 to the end 
                cost at 1 plus the cost from 3 to the end 

            3. likewise find 0 to the end is just 
                cost at 0 plus 1 to the end 
                cost at 0 plus 2 to the end

        '''
        #constant space sol
        #in relation to i, curr is i + 1 and prev is i + 2
        #curr holds the cost 
        curr = prev = 0

        for i in range(len(cost) - 1, -1, -1):
            temp = curr

            curr = cost[i] + min(temp, prev)

            prev = temp

        return min(curr, prev)