class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #stores the well formed parens that can be formed with n paiirs of paren
        res = []
        def backtrack(cand, open_ct, close_ct):
            #we have used n pairs of paren to form well formed seq of parens
            if len(cand) == n * 2:
                res.append("".join(cand.copy()))

            #if open_ct is < n
            if open_ct < n:
                cand.append("(")
                backtrack(cand, open_ct + 1, close_ct)
                cand.pop()
            
            if open_ct > close_ct:
                cand.append(")")
                backtrack(cand, open_ct, close_ct + 1)
                cand.pop()
        #cand is a list starting with an open paren allowing us to start off making a binary decision of including a open paren or a close paren
        backtrack(["("], 1, 0)
        return res
