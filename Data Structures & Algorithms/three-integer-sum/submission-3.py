class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            #all subsequent elements added 
            #with this element will always give us sum > 0 bc input is sorted
            if nums[i] > 0:
                break
            #we do not want duplicate solutions 
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            lo = i + 1
            hi = n - 1

            #lo and hi cannot be equal because all indices are DISTINCT
            while lo < hi:
                curr_sum = nums[i] + nums[lo] + nums[hi]

                if curr_sum == 0:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    #make sure lo and hi don't cross after the update
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1 
                elif curr_sum < 0:
                    #if we didn't find a solution and we encounter a 
                    #duplicate lo value we don't have to worry as this wouldn't give us 
                    #dup solutions -> freely move lo 
                    lo += 1
                elif curr_sum > 0:
                    #if we didn't find a solution and we encounter a 
                    #duplicate hi value we don't have to worry as this wouldn't give us 
                    #dup solutions -> freely move hi 
                    hi -= 1

        return res 