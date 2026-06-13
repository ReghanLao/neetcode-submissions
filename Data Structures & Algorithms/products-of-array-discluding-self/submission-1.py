class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_arr = [None] * n
        right_arr = [None] * n
        res = [None] * n 
        product = 1

        #building array containing product of everything to left of curr
        for i in range(n):
            left_arr[i] = product
            product *= nums[i]

        product = 1

        for i in range(n - 1, -1, -1):
            right_arr[i] = product 
            product *= nums[i]
        
        for i in range(n):
            res[i] = left_arr[i] * right_arr[i]
        
        return res

