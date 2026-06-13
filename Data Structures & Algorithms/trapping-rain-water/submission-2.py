class Solution:
    def trap(self, height: List[int]) -> int:
        #two ptrs move inward based on which is smaller(our calculations depend on bottle neck)
        left = 0 
        right = len(height) - 1
        res = 0 

        #we want to know whats locally our bottleneck height when computing water that can
        #be stored at left or right areas
        max_left = max_right = 0

        #we are done computing trapped water when finishing computations at left and right region 
        #aka when the ptrs cross
        while left < right:
            #compute the water that can be stored at left because left is our bottle neck
            if height[left] < height[right]:
                water_stored = max_left - height[left]
                if water_stored > 0:
                    res += water_stored
                max_left = max(max_left, height[left])
                left += 1
            else:
            #else we compute the water that can be stored at right because right is our bottleneck or we compute right by default
                water_stored = max_right - height[right]
                if water_stored > 0:
                    res += water_stored
                max_right = max(max_right, height[right])
                right -= 1
        
        return res 



