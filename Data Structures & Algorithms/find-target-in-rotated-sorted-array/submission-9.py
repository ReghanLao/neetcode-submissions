class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
            rotated sorted array -> split into two sorted halves or already sorted

            what marks where we should search? the minimum element as it marks the split or it marks the start of the search space when the array is just perfectly rotated n times 
        '''

        #find the index of the minimum element 
        left = 0 
        right = len(nums) - 1

        #left and right will converge on the min element index
        while left < right:
            mid = (left + right) // 2

            #smaller elements lie to right thus our min can be there
            if nums[mid] > nums[right]:
                left = mid + 1 
            #this can be our peak element or smaller to the left 
            else:
                right = mid 
        
        peak = left 

        #our peak converges to 0 if array is rotated n times 
        if peak == 0:
            l = 0 
            r = len(nums) - 1

            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
        elif nums[0] <= target <= nums[peak - 1]:
            l = 0 
            r = peak - 1

            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
        else:
            l = peak 
            r = len(nums) - 1

            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1

        return -1 
