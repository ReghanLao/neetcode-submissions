class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                #pivot occurs after mid
                left = mid + 1
            elif nums[mid] < nums[right]:
                #potential solution so narrow in here
                right = mid
        
        if left == right:
            return nums[left]