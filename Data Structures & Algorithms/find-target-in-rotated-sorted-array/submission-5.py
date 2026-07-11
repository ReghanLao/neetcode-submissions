class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
            1. our array can be rotated 1 to n-1 times
            2. our array can be rotated any multiple of n times

            notice that if our array is rotated then 
            it is split into two sorted halves

            lets determine the point of the split using BS 
            and run a BS on the both halvex to find the target

            to determine the point of pivot we must find 
            where the minimum element occurs 
        """

        left = 0 
        right = len(nums) - 1
        
        is_sorted = False

        while left < right: 
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] <= nums[right]:
                right = mid 
            
            if nums[mid] < nums[right] and nums[mid] > nums[left]:
                #array is already sorted 
                is_sorted = True      
                break 

        pivot = left
        print(pivot)
        print(is_sorted)
        if is_sorted:
            left = 0 
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return -1
        else:
            
            #explore left half
            left = 0
            right = pivot - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                
        #explore right half
            left = pivot 
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                
            return -1




