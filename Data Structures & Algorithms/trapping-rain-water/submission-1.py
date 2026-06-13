class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        
        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        total = 0 

        while left < right:
            #left_max is the bottle neck height
            #the max water level is determined by left_max so ignore right_max
            #the actual water that can be stored is left_max - height[left]
            if left_max < right_max:
                #increment left initially bc cannot store at initial
                #wall
                left += 1

                #update max immediately - current wall may be taller
                left_max = max(left_max, height[left])

                total += left_max - height[left]
            else:
                #decrement right initially bc cannot store at initial
                #wall
                right -= 1

                #update max immediately - current wall may be taller
                right_max = max(right_max, height[right])

                total += right_max - height[right]


        return total 

