class Solution:
    def mySqrt(self, x: int) -> int:
        #binary search -> because we are trying to find an integer from the range 0 to x
        #st that, that particular integer when multiplied by itself produces x 
        #what numbers in the range multiplied by itself will produce x?
        left = 0 
        right = x
        
        # 0 1 2 3 4 5 6 7 8 9 10 11 12 13

        while left <= right:
            mid = (left + right) // 2

            res = mid * mid 

            if res == x:
                return mid
            elif res > x:
                right = mid - 1
            else:
                left = mid + 1
        
        #in the end if the pointers cross that means we werent able to find a perfect integer multiplied by itself to get x
        #whats in left - 1 is the sqrt of x rounded down to the nearest integer because:

        #left is the smallest number whose square is > x
        #if we subtract 1 from this number we have the floor of the sqrt(x) which is what the problem is exactly asking for 
        return left - 1

        #time complexity: O(log(x))
        #space complexity: O(1)