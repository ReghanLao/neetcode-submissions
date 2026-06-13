class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        n = len(nums)
        right = left = 0
        res = []

        while right < n:
            while q and nums[right] > nums[q[-1]]:
                q.pop()

            q.append(right)

            while q[0] < left:
                q.popleft()
            
            if right - left + 1 >= k:
                res.append(nums[q[0]])
                left += 1
            right += 1
        
        return res
        

