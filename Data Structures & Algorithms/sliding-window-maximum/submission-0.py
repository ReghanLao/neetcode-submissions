import math

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #define initial window + initial max 
        max_element = -math.inf
        n = len(nums)
        left = 0

        max_element = max(nums[left:k])
        res = []
        res.append(max_element)

        for right in range(k, n):
            left += 1
            max_element = max(nums[left:right + 1])
            res.append(max_element)

        return res