class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1 
        if n == 2:
            return 2
        
        prev = 1
        curr = 2
        
        # n = 3, start : 1 2
        for i in range(2, n):
            # To reach step n, you must have come from: 
            # step n-1 (taking 1 step), or
            # step n-2 (taking 2 steps)
            prev, curr = curr, prev + curr
        #n = 3, end : 1 2 3
        return curr
