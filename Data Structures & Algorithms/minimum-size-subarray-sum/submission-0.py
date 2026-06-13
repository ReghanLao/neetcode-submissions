import math 
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #basically have a window slide over the input array
        #keep growing the window while the sum is < target
        #but while the sum is >= target then start shrinking the window from the left 
        #to try to find a more minimum window that holds the constraints 

        min_length = math.inf 
        left = 0 
        curr_sum = 0

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target: 
                #compute the length of curr window + try 
                #then try to shrink while maintaining property of curr sum needing to be >= target
                min_length = min(right - left + 1, min_length)

                curr_sum -= nums[left]
                left += 1
            
            print(min_length)
        
        #if our min length never changed then that means our sum thru our entire
        #array is less than our target so there is no such subarray
        if min_length == math.inf:
            min_length = 0
        
        return min_length 
