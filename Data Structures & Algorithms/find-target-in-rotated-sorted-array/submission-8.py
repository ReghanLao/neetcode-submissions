class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
            When an array is rotated it causes the array to be broken into 2 
            sorted halves 

            We also might have the case where an array was rotated a multiple 
            of n times so the array is technically already sorted 

            To determine if an array is broken up into two halves or not we
            need to run a BS to find the peak element which breaks the array
            into 2 halves. 

            Peak meaning minimum element 

            If the mid element is basically in sorted order already that
            means the array was rotated a multiple of n times 

            We are guaranteed to have unique elements in the array so that
            means we can find a unique mid element that breaks an array into 2 sorted halves and we can find a unique mid element that will tell us if we are rotated a multiple of n times 
        '''

        left = 0 
        right = len(nums) - 1

        #bs to find peak 
        while left < right:
            mid = (left + right) // 2
            
            #array is rotated a multiple of n times so technically sorted - perform a regular BS 
            if nums[0] < nums[mid] < nums[-1]:
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
            #if our middle element is greater than our last element our peak 
            #has to occur to the right as this structure tells us our peak is to the right 
            elif nums[mid] > nums[right]:
                left = mid + 1
            #our peak or min element is to the left but it could also be this element itself too
            elif nums[mid] < nums[right]:
                right = mid 
                
        
        #left and right converge on the peak aka the mid point 
        #determine which half to search 
        peak = left 
        
    #BS left to peak - 1
        left = 0 
        right = peak - 1

        while left <= right: 
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid 
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        #BS peak to right 


        left = peak 
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

                

