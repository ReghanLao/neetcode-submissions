class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        seen = set()
        left = 0
        right = 0
        n = len(nums)


        for right in range(n):
            #maintains a valid window 
            while (right - left > k):
                seen.remove(nums[left])
                left += 1

            #if element we are about to add has already been 
            #seen and is in valid window bounds then
            #both conditions satisfied            
            if nums[right] in seen:
                return True
            else:
                seen.add(nums[right])

        return False