class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #we will have two pointers for the left and right region 
        #everything after the left region will contain 0s 
        #everything after the right region will contain 2s
        #we wait before advancing our i ptr when we perform a swap with the right pointer
        #as it can contain 0,1,2 and can introduce 0s in the middle of our array which we will
        #need to swap again before advancing 
        #its safe to advance our i ptr however when swapping from left because at that point 
        #our left region will only have 0 or 1s as 2s would already be sent to the right 
        #basically placing a 0 or 1 in the middle is fine as that is where they typically are inserted 


        left = 0 
        right = len(nums) - 1
        i = 0 
        
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp 
        
        #stop iterating when i and right cross as array is sorted at this point 
        while i <= right: 
            if nums[i] == 0:
                swap(left, i)
                left += 1
                i += 1
            elif nums[i] == 2:
                swap(right, i)
                right -= 1 
            else: 
            #number is a 1 we can ignore and continue iterating as these 1s will naturally fall in place 
                i += 1 
        
                
        