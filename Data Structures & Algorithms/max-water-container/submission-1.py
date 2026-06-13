class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = -math.inf

        for i in range(n):
            for j in range(i + 1, n):
            #compute area for every single pair of heights -> area is limited by the bottleneck which is 
            #the shorter height of the pair 
                area = (j - i) * min(heights[i], heights[j])
                max_area = max(area, max_area)

        return max_area