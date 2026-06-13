class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #the product of a given element in a list except for itself
        #is the product of numbers to the left and right of the given element

        #build left array 
        left = [1]
        running_product = 1
        for i in range(1, len(nums)):
            running_product *= nums[i-1]
            left.append(running_product)
        
        #build right array 
        right = [1]
        running_product = 1
        for i in range(len(nums) - 2, -1, -1):
            running_product *= nums[i+1]
            right.insert(0, running_product)

        #build result array (left[i] * right[i])
        res = []
        for i in range(len(nums)):
            res.append(left[i] * right[i])
        
        return res
