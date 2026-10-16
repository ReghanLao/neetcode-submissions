class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        '''
            Same logic as Search In Rotated Sorted Array 1

            However if nums[mid] == nums[right] - we can't determine which half is sorted as dups can exist in both halves we need to remove the dup from this right half first to determine which half is sorted
        '''


        left = 0 
        right = len(nums) - 1


        while left <= right:
            mid = (left + right) // 2


            if nums[mid] == target:
                return True
            #cant determine which half is sorted we go next and remove thing that clouds us
            elif nums[mid] == nums[right]:
                right -= 1
            #left half sorted
            elif nums[mid] > nums[right]:
                #already checked for inclusivity at mid in first if 
                #if in this range then search this half else search right half 
                #use sorted nature to figure if its even in this half 
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            #right half sorted
            else:
                #In right half 
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False


