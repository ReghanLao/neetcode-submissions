class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the pivot point as this is where the two halves form

        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        min_index = left 

        #if the pivot point occurs at index 0 or the start we know
        #the array is already sorted so perform binary search as usual
        #else the pivot point forms two halves so perform binary search 
        #on one of those two halves 

        if min_index == 0:
            left = 0
            right = n - 1
        elif target >= nums[0] and target <= nums[min_index - 1]:
            left = 0
            right = min_index - 1
        else:
            left = min_index
            right = n - 1
        
        #perform binary search with the correct bounds 
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1