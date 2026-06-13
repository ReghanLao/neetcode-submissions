class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #basically the whole idea is to use a sliding window check over a range
        #of indices (satisfying the difference in range condition) and also checking
        #in the particular window if there is a duplicate if so then we have met 
        #our condition 

        left = 0 
        seen = set()
        for right in range(len(nums)):
            #we alter our window bounds if condition (range) is violated
            while (right - left) > k:
                seen.remove(nums[left])
                left += 1
            
            #basically if there is a nums[i] and nums[j] in the range that are dups
            if nums[right] in seen:
                return True 

            seen.add(nums[right])
        
        return False 


