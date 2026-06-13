class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_mul = 1
        right_mul = 1
        left_arr = [0] * len(nums)
        right_arr = [0] * len(nums)
        res = [0] * len(nums)

        #build left array
        for i in range(len(nums)):
            left_arr[i] = left_mul
            left_mul *= nums[i]
        
        #build right array
        for i in range(len(nums) - 1, -1, -1):
            right_arr[i] = right_mul
            right_mul *= nums[i]

        #build res array
        for i in range(len(nums)):
            res[i] = left_arr[i] * right_arr[i]

        return res