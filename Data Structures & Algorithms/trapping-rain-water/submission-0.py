import math 

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        total_water = 0
        left = 0
        right = len(height) - 1
        left_max = height[0]
        right_max = height[len(height) - 1]

        while left < right:
            if height[left] < height[right]:
                #we know that the left is the bottleneck 
                if height[left] >= left_max:
                    #update our left max if our current height at left is greater
                    #can't store water here 
                    left_max = height[left]
                else: 
                    #our current height is less than bottle neck (left_max) so we can put water here
                    total_water += left_max - height[left]
                
                left += 1

            else:
                # we know that the right is the bottle neck or they are the same so we move right by default
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    # our current height is less than bottle neck (right max) so we can put water here
                    total_water += right_max - height[right]
                right -= 1

        return total_water




