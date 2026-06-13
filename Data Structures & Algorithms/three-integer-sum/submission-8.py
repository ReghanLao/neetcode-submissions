class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #in order to utilize two pointers we must sort array 
        #whole idea is to fix a starting value and start two pointers:
        #one ptr after fixed value and another pointer and the end 
        #find a triplet that sums to 0, however we want to avoid duplicate
        #triplets therefore we must skip over duplicate fixed values 
        #(if we find a sol for this fixed val it skips over potential dup, but we
        #didn't find sol for this fixed val we would skip over a iteration that doesn't produce results which is fine
        #we must also continue incrementing when left and right ptr land on same value to prevent producing more dups 

        nums.sort()
        res = []
        #i represents fixed ptr 
        for i in range(len(nums)):
            if nums[i] > 0:
                break 
            
            #avoids dup trip thru avoiding dup fixed val 
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            left = i + 1
            right = len(nums) - 1
            
            while left < right: 
                #test triplet 
                trip_sum = nums[i] + nums[left] + nums[right]

                if trip_sum == 0: 
                    res.append([nums[i], nums[left], nums[right]])

                    #increment left and decrement right ptr 
                    left += 1
                    right -= 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                elif trip_sum > 0:
                    right -= 1
                elif trip_sum < 0:
                    left += 1

        return res
            
