class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        # i will represent fixed - go thru every fixed and find potential
        #valid triplet summing to 0 
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue 

            left = i + 1
            right = n - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    #found a sol so update left and right accordingly
                    left += 1
                    right -= 1
    
                    #we want to make sure that left and right don't land
                #at the same value they were previously at before 
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1

        return res 
