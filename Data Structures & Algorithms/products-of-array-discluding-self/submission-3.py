class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
            we can take the product of everything:
                1. before i 
                2. after i 
                
            and multiply it together to get the product of everything besides i 
            at any given i 
        '''

        #build before i array
        before = [0] * len(nums)
        curr = 1
        for i in range(len(nums)):
            before[i] = curr
            curr *= nums[i]

        #build after i array 
        after = [0] * len(nums)
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            after[i] = curr
            curr *= nums[i]

        #multiply both before and after together to get resulting array aka array with product except self 
        res = [0] * len(nums)

        for i in range(len(res)):
            res[i] = after[i] * before[i]
        return res