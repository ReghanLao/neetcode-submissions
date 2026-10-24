class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
            Return all well formed paren -> generate all well formed paren
            combinations -> backtracking possible since 
            small n

            Backtrack is bounded by two choices

            1. Ability to place open paren
            2. Ability to place close paren

            Note:

            We can only place open parenthesis if the amount of less than n

            We can only place a close parenthesis in the sequence if the 
            there is something to close aka open ct > close ct
        '''

        #stores all well formed paren combos
        res = []
        
        #cand stores the singular current well formed paren combo 
        def backtrack(cand, open_ct, close_ct):
            #we have a solution as we have used n open paren and n close paren 
            if len(cand) == n * 2:
                res.append("".join(cand.copy()))
                return 
            
            #we can only open if open_ct < n
            if open_ct < n:
                cand.append('(')
                backtrack(cand, open_ct + 1, close_ct)
                cand.pop()
                
            #we can only close if we have more open paren than close
            if close_ct < open_ct:
                cand.append(')')
                backtrack(cand, open_ct, close_ct + 1)
                cand.pop()
            
            



        
        #start with an open paren allows us to go with the binary logic of choosing to put down open paren and choosing to put down close paren
        backtrack(['('], 1, 0)

        return res


        