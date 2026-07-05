class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
            Two cases:
            1. Array is rotated 1 to n - 1 times - [3,4,5,6,1,2]
            2. Array is rotated a multiple of n times 
            - [1,2,3,4,5,6]

            In the rotated case we can run a BS and compute the midpoint 
            and take a note of where we are 

            If we are in the left half we want to search right - these
            are where the smaller values live 

            If we are in the right half we want to search left - we 
            can find a smaller value somewhere in the left half including
            the current range we are in because or min could actually
            be in this current range too 
    
        '''

        left = 0 
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2 
            
            #if this middle element is greater than or equal to the first and 
            #less than or equal to the last this array is sorted so return
            #nums[0]
            if nums[mid] >= nums[0] and nums[mid] <= nums[-1]:
                return nums[0]
            #we are in the left half somewhere and smaller elements live in the right
            elif nums[mid] >= nums[0]:
                left = mid + 1
            #we are in the right half somewhere and smaller elements could live somewhere in the left
            elif nums[mid] <= nums[-1]:
                right = mid 
            
        #at the end our left and right ptrs should converge on the min
        return nums[left]
        

        