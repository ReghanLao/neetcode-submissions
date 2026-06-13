class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = right = 1

        # we know that the first element is unique there for we start
        # the two ptrs at 1
        # by default we will have one unique element 

        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        
        return left 