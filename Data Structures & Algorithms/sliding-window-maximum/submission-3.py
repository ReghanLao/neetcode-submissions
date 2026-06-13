import collections 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = [] #array to store maximum element in the window at each step
        left = right = 0 #window boundaries 

        #will be monotonically decreasing so that
        #index corresponding to largest element will be stored at the front
        #prevents any repeated work in finding the max 
        #by removing smaller elements which could never ever be the max
        q = collections.deque()

        while right < len(nums):
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            q.append(right)

            if q[0] < left:
                q.popleft()
            
            if (right - left + 1) == k:
                output.append(nums[q[0]])
                left += 1
            
            right += 1
        
        return output






