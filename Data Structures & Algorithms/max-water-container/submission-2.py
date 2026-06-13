class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = -math.inf
        left = 0
        right = n - 1

        while left < right:
            area = (right - left) * min(heights[left], heights[right])

            if heights[right] > heights[left]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                right -= 1 
            
            max_area = max(area, max_area)

        return max_area