class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
            The amount of water that can be confined between 
            two pillars is defined by the height of the confinement
            x the width of the confinement 

            One approach to brute force check every confinement 
            defined by every possible pair of pillars -> n^2 sol

            A better approach is to maximize the width and height by
            starting at the very ends selecting the outer most pillars
            and then to maximize the height keep checking other pillars
            against the current tallest pillar 

            By doing this we are able to initally maximize width
            and we are able to maximize height 
        '''

        left = 0 
        right = len(heights) - 1
        most_water = -float('inf')

        while left < right:
            #distance between two bars
            width = right - left
            #the shorter pillar is the bottle neck for how much water we
            #are able to store in a container
            height = min(heights[left], heights[right])
            water = width * height

            most_water = max(water, most_water)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return most_water
