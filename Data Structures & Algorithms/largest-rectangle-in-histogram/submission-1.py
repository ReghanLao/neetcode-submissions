class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] #will contain index, height pairs 

        for i, h in enumerate(heights):
            start = i 

            while stack and stack[-1][1] > h:
                #we cannot extend previous bar any further
                #pop this bar from stack
                #compute the area made possible by this bar
                #extend current bar back
                index, height = stack.pop()
                area = height * (i - index)
                start = index
                max_area = max(max_area, area)
        
            stack.append((start, h))

        for i, h in stack:
            area = h * (len(heights) - i)
            max_area = max(max_area, area)

        return max_area
            
